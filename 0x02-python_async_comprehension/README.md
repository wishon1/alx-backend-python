# 0x02. Python - Async Comprehension

## Resources
Read or watch:
- [PEP 530 – Asynchronous Comprehensions](https://peps.python.org/pep-0530/)
- [What’s New in Python: Asynchronous Comprehensions / Generators](https://docs.python.org/3/whatsnew/3.6.html#asynchronous-comprehensions)
- [Type-hints for generators](https://docs.python.org/3/library/typing.html#typing.Generator)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

## Requirements
### General
- **Allowed Editors**: vi, vim, emacs
- **Interpreter/Compiler**: Ubuntu 18.04 LTS using python3 (version 3.7)
- **End of File**: All files should end with a new line
- **Shebang**: The first line of all files should be exactly `#!/usr/bin/env python3`
- **README.md**: A README.md file, at the root of the folder of the project, is mandatory
- **Code Style**: Your code should use the pycodestyle style (version 2.5.x)
- **File Length**: The length of your files will be tested using wc
- **Documentation**: All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- **Function Documentation**: All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- **Meaningful Documentation**: A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- **Type Annotations**: All your functions and coroutines must be type-annotated.

### Tasks
1. **Async Generator**
   - Write a coroutine called `async_generator` that takes no arguments.
   - The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10.
   - Use the `random` module.

2. **Async Comprehensions**
   - Import `async_generator` from the previous task and then write a coroutine called `async_comprehension` that takes no arguments.
   - The coroutine will collect 10 random numbers using an async comprehension over `async_generator`, then return the 10 random numbers.

3. **Run time for four parallel comprehensions**
   - Import `async_comprehension` from the previous file and write a `measure_runtime` coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather`.
   - `measure_runtime` should measure the total runtime and return it.
   - Notice that the total runtime is roughly 10 seconds, explain it to yourself.

## Repository
- **GitHub Repository**: [alx-backend-python](https://github.com/wishon1/alx-backend-python)
- **Directory**: 0x02-python_async_comprehension

## Files
1. **0-async_generator.py**
2. **1-async_comprehension.py**
3. **2-measure_runtime.py**
