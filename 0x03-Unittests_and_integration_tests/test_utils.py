#!/usr/bin/env python3
"""Module to parameterize unit tests."""

from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
import unittest
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """Test suite for access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test that access_nested_map returns the correct value.

        Args:
            nested_map (dict): The dictionary to access.
            path (tuple): The path of keys to navigate through the nested_map.
            expected: The expected value to be returned.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        Test that access_nested_map raises a KeyError for invalid paths.

        Args:
            nested_map (dict): The dictionary to access.
            path (tuple): The path of keys to navigate through the nested_map.
            expected: The expected key that raises the KeyError.
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test suite for get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test that get_json returns the correct JSON response.

        Args:
            test_url (str): The URL to fetch the JSON from.
            test_payload (dict): The expected JSON payload.
        """
        # Mock the requests.get method to return a custom response
        mock_response_config = {'return_value.json.return_value': test_payload}
        mock_requests_get = patch('requests.get', **mock_response_config)
        mock_get = mock_requests_get.start()

        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)

        mock_requests_get.stop()


class TestMemoize(unittest.TestCase):
    """Test suite for memoize decorator."""

    def test_memoize(self):
        """Test that memoize caches the result of a method."""

        class TestClass:
            """Class for testing the memoize decorator."""

            def a_method(self):
                """A method that returns a fixed value."""
                return 42

            @memoize
            def a_property(self):
                """A property method decorated with memoize."""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_a_method:
            test_class = TestClass()
            # Call the memoized property twice
            test_class.a_property()
            test_class.a_property()

            # Verify that a_method is only called once
            mock_a_method.assert_called_once()
