#!/usr/bin/env python3
""" Module for testing the GithubOrgClient class """

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
import json
import unittest
from unittest.mock import patch, PropertyMock, Mock


class TestGithubOrgClient(unittest.TestCase):
    """ Class for testing the GithubOrgClient """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct organization data.

        Args:
            org_name (str): The name of the GitHub organization.
            mock_get_json (Mock): The mocked get_json method.
        """
        github_client = GithubOrgClient(org_name)
        github_client.org()
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}')

    def test_public_repos_url(self):
        """
        Test that the _public_repos_url property returns the correct URL
        based on the mocked organization payload.
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as context:
            org_payload = \
                {"repos_url": "https://api.github.com/orgs/test/repos"}
            context.return_value = org_payload
            github_client = GithubOrgClient('test')
            repos_url = github_client._public_repos_url
            self.assertEqual(repos_url, org_payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test that public_repos returns the list of repository names and that
        the mocked _public_repos_url property and get_json method are called
        once.

        Args:
            mock_get_json (Mock): The mocked get_json method.
        """
        repos_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_get_json.return_value = repos_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_repos_url:
            mock_repos_url.return_value =\
                "https://api.github.com/orgs/test/repos"
            github_client = GithubOrgClient('test')
            repo_names = github_client.public_repos()
            expected_repo_names = [repo["name"] for repo in repos_payload]
            self.assertEqual(repo_names, expected_repo_names)
            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test that has_license correctly checks for the presence of a license
        key in a repository.

        Args:
            repo (dict): The repository data.
            license_key (str): The license key to check for.
            expected (bool): The expected result.
        """
        has_license_result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(has_license_result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Class for integration tests of GithubOrgClient using fixtures """

    @classmethod
    def setUpClass(cls):
        """Set up class method for initializing test environment before
        running tests."""
        config = {
            'return_value.json.side_effect': [
                cls.org_payload, cls.repos_payload,
                cls.org_payload, cls.repos_payload
            ]
        }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock_get = cls.get_patcher.start()

    def test_public_repos(self):
        """Integration test for public_repos method."""
        github_client = GithubOrgClient("google")
        self.assertEqual(github_client.org, self.org_payload)
        self.assertEqual(github_client.repos_payload, self.repos_payload)
        self.assertEqual(github_client.public_repos(), self.expected_repos)
        self.assertEqual(github_client.public_repos("XLICENSE"), [])
        self.mock_get.assert_called()

    def test_public_repos_with_license(self):
        """Integration test for public_repos method with license filtering."""
        github_client = GithubOrgClient("google")
        self.assertEqual(github_client.public_repos(), self.expected_repos)
        self.assertEqual(github_client.public_repos("XLICENSE"), [])
        self.assertEqual(github_client.public_repos("apache-2.0"),
                         self.apache2_repos)
        self.mock_get.assert_called()

    @classmethod
    def tearDownClass(cls):
        """Tear down class method for cleaning up after tests are run."""
        cls.get_patcher.stop()
