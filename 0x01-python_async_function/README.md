# alx-backend-python

## Resources

### Read or Watch
- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)

## Learning Objectives

By the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- `async` and `await` syntax
- How to execute an async program with `asyncio`
- How to run concurrent coroutines
- How to create asyncio tasks
- How to use the `random` module

## Requirements

### General
- A `README.md` file, at the root of the folder of the project, is mandatory
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All your files should end with a new line
- All your files must be executable
- The length of your files will be tested using `wc`
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- Your code should use the `pycodestyle` style (version 2.5.x)
- All your functions and coroutines must be type-annotated.
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class, or method (the length of it will be verified)

### Tasks
#### 0. The basics of async
- Write an asynchronous coroutine named `wait_random` that takes in an integer argument `max_delay` (with a default value of 10) and waits for a random delay between 0 and `max_delay` (included and float value) seconds and eventually returns it.
- Use the `random` module.

#### 1. Let's execute multiple coroutines at the same time with async
- Import `wait_random` from the previous python file and write an async routine called `wait_n` that takes in 2 int arguments `n` and `max_delay`. You will spawn `wait_random` `n` times with the specified `max_delay`.
- `wait_n` should return the list of all the delays (float values). The list of the delays should be in ascending order without using `sort()` because of concurrency.

#### 2. Measure the runtime
- From the previous file, import `wait_n` into `measure_runtime.py`.
- Create a `measure_time` function with integers `n` and `max_delay` as arguments that measures the total execution time for `wait_n(n, max_delay)`, and returns `total_time / n`. Your function should return a float.

#### 3. Tasks
- Import `wait_random` from `0-basic_async_syntax.py`.
- Write a function (do not create an async function, use the regular function syntax to do this) `task_wait_random` that takes an integer `max_delay` and returns a `asyncio.Task`.

#### 4. Tasks
- Take the code from `wait_n` and alter it into a new function `task_wait_n`. The code is nearly identical to `wait_n` except `task_wait_random` is being called.

## Repo Details

- GitHub repository: [alx-backend-python](https://github.com/wishon1/alx-backend-python)
- Directory: `0x01-python_async_function`
- Files:
  - `0-basic_async_syntax.py`
  - `1-concurrent_coroutines.py`
  - `2-measure_runtime.py`
  - `3-tasks.py`
  - `4-tasks.py`

---

Feel free to reach out if you have any questions or need further clarification!
