# Tasks

## 0. Run Python file

Write a Shell script that runs Python code that will be saved in the environment variable `$PYFILE`

`export PYFILE=main.py`

File: [0-run](./0-run), [main.py](./main.py)

## 1. Run inline

Write a Shell script that runs Python code that will be saved in the environment variable `$PYCODE`

`export PYCODE='print(f"Best School: {88+10}")'`

File: [1-run_inline](./1-run_inline)

## 2. Hello, print

Write a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.

File: [2-print.py](./2-print.py)

## 3. Print integer

Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.

File: [3-print_number.py](./3-print_number.py)

## 4. Print float

Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py) in order to print the float stored in the variable `number` with a precision of 2 digits.

File: [4-print_float.py](./4-print_float.py)

## 5. Print string

Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py) in order to print 3 times a string stored in the variable `str`, followed by its first 9 characters.

File: [5-print_string.py](./5-print_string.py)

## 6. Play with strings

Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py) to print `Welcome to Holberton School!`

File: [6-concat.py](./6-concat.py)

## 7. Copy - Cut - Paste

Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py)

* `word_first_3` should contain the first 3 letters of the variable word

* `word_last_2` should contain the last 2 letters of the variable word

* `middle_word` should contain the value of the variable word without the first and last letters

File: [7-edges.py](./7-edges.py)

## 8. Create a new sentence

Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py) to print object-oriented programming with Python, followed by a new line.

* You are not allowed to use any loops or conditional statements

* Your program should be exactly 5 lines long

* You are not allowed to create new variables

* You are not allowed to use string literals

File: [8-concat_edges.py](./8-concat_edges.py)

## 9. Easter Egg

Write a Python script that prints `"The Zen of Python", by TimPeters`, followed by a new line

* Script should  be maximum 98 characters long (please check with `wc -m 9-easter_egg.py`)

File: [9-easter_egg.py](./9-easter_egg.py)

## 10. Linked list cycle (Technical interview preparation)

Write a function in C that checks if a singly linked list has a cycle in it.

* Prototype: `int check_cycle(listint_t *list);`

* Return: 0 if there is no cycle, 1 if there is a cycle

`gcc -Wall -Werror -Wextra -pedantic -std=gnu89 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle`

Requirements

* Allowed functions: `write`, `printf`, `putchar`, `puts`, `malloc`, `free`

Files: [10-check_cycle.c](./10-check_cycle.c), [lists.h](./lists.h)

## 11. Hello, write

Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.

* Use the function `write` from the `sys` module

* You are not allowed to use `print`

* Your script should print to `stderr`

* Your script should exit with the status code `1`

File: [100-write.py](./100-write.py)

## 12. Compile

A script that compiles a Python script file.

The Python file name will be stored in the environment variable `$PYFILE`

The output filename has to be `$PYFILEc` (ex: `export PYFILE=my_main.py` => output filename: `my_main.pyc`)

File: [101-compile](./101-compile)

## 13. ByteCode -> Python #1 

Write the Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:

`3           0 LOAD_CONST               1 (98)

            3 LOAD_FAST                0 (a)

            6 LOAD_FAST                1 (b)

            9 BINARY_POWER

           10 BINARY_ADD

           11 RETURN_VALUE
`

* Tip: [Python bytecode](https://docs.python.org/3.4/library/dis.html)

File: [102-magic_calculation.py](./102-magic_calculation.py)

# Resources

[An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html)

[How to use String Formatters in Python 3](https://realpython.com/python-f-strings/)

