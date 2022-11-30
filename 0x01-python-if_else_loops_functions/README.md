# Tasks

## 0. Positive anything is better than negative nothing

This program will assign a random signed number to the variable `number` each time it is executed. Complete the [source code](https://github.com/holbertonschool/0x01.py/blob/master/0-positive_or_negative_py) in order to print whether the number stored in the variable number is positive or negative.

The output of the program should be: The number, followed by, if the number is greater than 0: is positive, if the number is 0: is zero if the number is less than 0: is negative

**File**: [0-positive_or_negative.py](./0-positive_or_negative.py)

## 1. The last digit

This program will assign a random signed number to the variable `number` each time it is executed. Complete the [source code](https://github.com/holbertonschool/0x01.py/blob/master/1-last_digit_py) in order to print the last digit of the number stored in the variable number

**File**: [1-last_digit.py](./1-last_digit.py)

## 2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game

Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

* You can only use one print function with string format
* You can only use one loop in your code
* You are not allowed to store characters in a variable
* You are not allowed to import any module

**File**: [2-print_alphabet.py](./2-print_alphabet.py)

## 3. When I was having that alphabet soup, I never thought that it would pay off

Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

* Print all the letters except `q` and `e`
* You can only use one `print` function with string format
* You can only use one loop in your code
* You are not allowed to store characters in a variable
* You are not allowed to import any module

**File**: [3-print_alphabt.py](./3-print_alphabt.py)

## 4. Hexadecimal printing

Write a program that prints all numbers from `0` to `98` in decimal and in hexadecimal (as in the following example)

* You can only use one `print` function with string format
* You can only use one loop in your code
* You are not allowed to store numbers or strings in a variable
* You are not allowed to import any module

**File**: [4-print_hexa.py](./4-print_hexa.py)

## 5. 00...99

Write a program that prints all numbers from `0` to `98`

* Numbers must be separated by `,`, followed by a space
* Numbers should be printed in ascending order, with two digits
* The last number should be followed by a new line
* You can only use no more than 2 `print` functions with string format
* You can only use one loop in your code
* You are not allowed to store numbers or strings in a variable
* You are not allowed to import any module

**File**: [5-print_comb2.py](./5-print_comb2.py)

## 6. Inventing is a combination of brains and materials. The more brains you use, the less material you need

Write a program that prints all possible different combinations of two digits.

* Numbers must be separated by `,`, followed by a space
* The two digits must be different
* `01` and `10` are considered the same combination of the two digits `0` and `1`
* Print only the smallest combination of two digits
* Numbers should be printed in ascending order, with two digits
* The last number should be followed by a new line
* You can only use no more than 3 `print` functions with string format
* You can only use no more than 2 loops in your code
* You are not allowed to store numbers or strings in a variable
* You are not allowed to import any module

**File**: [6-print_comb3.py](./6-print_comb3.py)

## 7. islower

A function that checks for lowercase character.

* Prototype: `def islower(c):`
* Returns `True` if `c` is lowercase
* Returns `False` otherwise
* You are not allowed to import any module
* You are not allowed to use `str.upper()` and `str.isupper()`
* Tips: [ord()](https://docs.python.org/3.4/library/functions.html?highlight=ord#ord)

`$ ./7-main.py`

**File**: [7-islower.py](./7-islower.py), [7-main.py](./7-main.py)

## 8. To uppercase

A function that prints a string in uppercase followed by a new line.

* Prototype: `def uppercase(str):`
* You can only use no more than 2 `print` functions with string format
* You can only use one loop in your code
* You are not allowed to import any module
* You are not allowed to use `str.upper()` and `str.isupper()`
* Tips: [ord()](https://docs.python.org/3.4/library/functions.html?highlight=ord#ord)

**File**: [8-uppercase.py](./8-uppercase.py)

## 9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important

A function that prints the last digit of a number.

* Prototype: `def print_last_digit(number):`
* Returns the value of the last digit
* You are not allowed to import any module

**File**: [9-print_last_digit.py](./9-print_last_digit.py)

## 10. a + b

A function that adds two integers and returns the result.

* Prototype: `def add(a, b):`
* Returns the value of `a + b`
* You are not allowed to import any module

**File**s: [10-add.py](./10-check_cycle.cadd.py)

## 11. a ^ b

A function that computes `a` to the power of `b` and return the value.

* Prototype: `def pow(a, b):`
* Returns the value of `a ^ b`
* You are not allowed to import any module

**File**: [11-pow.py](./11-pow.py)

## 12. Fizz Buzz

A function that prints the numbers from 1 to 100 separated by a space.

* For multiples of three print `Fizz` instead of the number and for multiples of five print `Buzz`.
* For numbers which are multiples of both three and five print `FizzBuzz`.
* Prototype: `def fizzbuzz():`
* Each element should be followed by a space
* You are not allowed to import any module

**File**: [12-fizzbuzz](./12-fizzbuzz)

## 13. Insert in sorted linked list (Technical interview preparation)

A function in C that inserts a number into a sorted singly linked list.

* Prototype: `listint_t *insert_node(listint_t **head, int number);`
* Return: the address of the new node, or `NULL` if it failed

`gcc -Wall -Werror -Wextra -pedantic -std=gnu89 13-main.c linked_lists.c 13-insert_number.c -o insert`

**File**: [13-insert_number.c](./13-insert_number.c), [lists.h](./lists.h)

# Resources

## Read

[More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)

[How to use string formatters in Python3](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)

## Watch

[IndentationError](https://www.youtube.com/watch?v=1QXOd2ZQs-Q)