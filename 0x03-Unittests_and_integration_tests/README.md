
## 0x03. Unittests and Integration Tests

`UnitTests` `Back-end` `Integration tests`

### Preview

Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.

The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

Integration tests will test interactions between every part of your code.

Execute your tests with

`$ python -m unittest path/to/test_file.py`

### Resources
- Read or watch:

* [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
* [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)
* [How to mock a readonly property with mock?](https://stackoverflow.com/questions/11836436/how-to-mock-a-readonly-property-with-mock)
* [parameterized](https://pypi.org/project/parameterized/)
* [Memoization](https://en.wikipedia.org/wiki/Memoization)

### Learning Objectives
- At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- The difference between unit and integration tests.
- Common testing patterns such as mocking, parametrizations and fixtures

### Required Files
[utils.py](github.com/wishon1/alx-backend-python/0x03-Unittests_and_integration_tests/utils.py)
[client.py](0x03-Unittests_and_integration_tests/client.py)
[fixtures.py](github.com/wishon1/alx-backend-python/0x03-Unittests_and_integration_tests/fixtures.py)

### Tasks
0. Parameterize a unit test
- Familiarize yourself with the `utils.access_nested_map` function and understand its purpose. Play with it in the Python console to make sure you understand.

- In this task you will write the first unit test for `utils.access_nested_map`.
- Create a TestAccessNestedMap class that inherits from `unittest.TestCase`.
- Implement the `TestAccessNestedMap.test_access_nested_map` method to test that the method returns what it is supposed to.
- Decorate the method with `@parameterized.expand` to test the function for following inputs:
```
nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
```
For each of these inputs, test with `assertEqual` that the function returns the expected result.
The body of the test method should not be longer than 2 lines.

- File: [test_utils.py](github.com/wishon1/alx-backend-python/0x03-Unittests_and_integration_tests/test_util.py)

1. Parameterize a unit test
- Implement `TestAccessNestedMap.test_access_nested_map_exception`. Use the `assertRaises` context manager to test that a `KeyError` is raised for the following inputs (use `@parameterized.expand`):
```
nested_map={}, path=("a",)
nested_map={"a": 1}, path=("a", "b")
```
Also make sure that the exception message is as expected.
- File: [test_utils.py](github.com/wishon1/alx-backend-python/0x03-Unittests_and_integration_tests/test_util.py)
