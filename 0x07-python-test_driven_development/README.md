# Test-driven development
![ttd](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/246/giphy-4.gif)

## Resources
* [doctest — Test interactive Python examples](https://docs.python.org/3.4/library/doctest.html)(until “26.2.3.7. Warnings” included)
* [doctest – Testing through documentation](https://pymotw.com/3/doctest/)
* [Unit Tests in Python](https://www.youtube.com/watch?v=1Lfv5tUGsn8)
* [Unittest module](https://www.youtube.com/watch?v=6tNS--WetLI)
* [Interactive and Non-interactive tests](https://mattermost.com/blog/testing-python-understanding-doctest-and-unittest/)

## Tasks
### 0. Integer addition
Function that adds 2 integers.

**File**: [0-add_integer.py](./0-add_integer.py), [tests/0-add_integer.txt](./tests/0-add_integer.txt)

### 1. Divide a matrix
Function that divides all elements of a matrix.

**File**: [2-matrix_divided.py](./2-matrix_divided.py), [tests/2-matrix_divided.txt](./tests/2-matrix_divided.txt)

### 2. Say my name
Function that prints `My name is <first name> <last name>`

**File**: [3-say_my_name.py](./3-say_my_name.py), [tests/3-say_my_name.txt](./tests/3-say_my_name.txt)

### 3. Print square
Function that prints a square with the character `#`.

**File**: [4-print_square.py](./4-print_square.py), [tests/4-print_square.txt](./tests/4-print_square.txt)

### 4. Text indentation
Function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`

**File**: [5-text_indentation.py](./5-text_indentation.py), [tests/5-text_indentation.txt](./tests/5-text_indentation.txt)

### 5.Max integer - Unittest
Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.

In this task, you will write unittests for the function `def max_integer(list=[]):`
* Your test file should be inside a folder `tests`
* You have to use the `unittest module`
* Your test file should be python files (extension: `.py`)
* Your test file should be executed by using this command: `python3 -m unittest tests.6-max_integer_test`