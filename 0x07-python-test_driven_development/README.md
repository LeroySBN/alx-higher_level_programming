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

### 5. Max integer - Unittest
Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.

In this task, you will write unittests for the function `def max_integer(list=[]):`
* Your test file should be inside a folder `tests`
* You have to use the `unittest module`
* Your test file should be python files (extension: `.py`)
* Your test file should be executed by using this command: `python3 -m unittest tests.6-max_integer_test`

**File**: [tests/6-max_integer_test.py](./tests/6-max_integer_test.py)

### 6. Matrix multiplication
A function that multiplies 2 matrices.

**File**: [100-matrix_mul.py](./100-matrix_mul.py), [tests/100-matrix_mul.txt](./tests/100-matrix_mul.txt)

### 7. Lazy matrix multiplication
A function that multiplies 2 matrices using the module `Numpy`

**File**: [101-lazy_matrix_mul.py](./101-lazy_matrix_mul.py), [tests/101-lazy_matrix_mul.txt](./tests/101-lazy_matrix_mul.txt)

### 8.CPython #3: Python Strings
![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/2c4f2b92514745519f833afdf5bc5f3eaff8c6ca.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230115%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230115T153640Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=84cbc693cc97f88a4f503fb7f6bba462139f0dbe533ef87fc62fb5047b3b781b)

A function that prints Python strings:
* Prototype: `void print_python_string(PyObject *p);`
* if p is not a valid string, print an error message
* Read: `[Unicode HOWTO](https://docs.python.org/3.4/howto/unicode.html)
* The shared library will be compiled with this command line: `gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c`

**File**: [102-python.c](./102-python.c)
