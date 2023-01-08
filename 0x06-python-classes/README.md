# Classes and Objects

![oop](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/247/oop-meme.jpg)

## Resources
### read
* [Object Oriented Programming](https://python.swaroopch.com/oop.html)
* [More Object Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php)
* [Properties vs Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
### watch
* [Learn to Program 9: Object Oriented Programming](https://www.youtube.com/watch?v=1AGyBuVCTeE&)
* [Python Classes and Objects](https://www.youtube.com/watch?v=apACNr7DC_s)
* [Object Oriented Programming](https://www.youtube.com/watch?v=-DP1i2ZU9gk)

## Tasks
### 0. My first square
An empty class `Square` that defines a square

**File**: [0-square.py](./0-square.py)

### 1. Square with size
A class `Square` that defines a square by a private instance attribute `size`, instantiation with `size` (no type/value verification).

**File**: [1-square.py](./1-square.py)

### 2. Size validation
A class `Square` that defines a square by, private instance attribute `size`, instantiation with optional `size`: `def __init__(self, size=0):`
* `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
* if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`

**File**: [2-square.py](./2-square.py)

### 3. Area of a square
A class Square that defines a square by a private instance attribute `size`, instantiation with optional `size`: `def __init__(self, size=0):` 
* size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
* if size is less than 0, raise a ValueError exception with the message size must be >= 0
Public instance method: def area(self): that returns the current square area

**File**: [3-square.py](./3-square.py)

### 4. Access and update private attribute
A class Square that defines a square by a private instance attribute `size`, property `def size(self):` to retrieve it, property setter `def size(self, value):` to set it (`size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`, if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`). Instantiation with optional `size`: `def __init__(self, size=0):`, public instance method: `def area(self):` that returns the current square area.

**File**: [4-square.py](./4-square.py)

### 5. Printing a square
A class `Square` that defines a square by a private instance attribute `size`, property `def size(self):` to retrieve it, property setter `def size(self, value):` to set it (`size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`. If `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`). Instantiation with optional `size`: `def __init__(self, size=0):`. Public instance method: `def area(self):` that returns the current square area. Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`: (if `size` is equal to 0, print an empty line.

**File**: [5-square.py](./5-square.py)

### 6. Coordinates of a square
A  class Square that defines a square by a private instance attribute: `size`: property `def size(self):` to retrieve it, property setter `def size(self, value):` to set it (`size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`. if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`). Private instance attribute: `position` with property `def position(self):` to retrieve it, property setter `def position(self, value):` to set it (`position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integers`). Instantiation with optional `size` and optional `position`: `def __init__(self, size=0, position=(0, 0)):`. Public instance method: `def area(self):` that returns the current square area. Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:(if `size` is equal to 0, print an empty line, `position` should be use by using space - Don’t fill lines by spaces when `position[1] > 0`

**File**: [6-square.py](./6-square.py)

### 7. Singly linked list
A class that defines a node of a singly linked list.

**File**: [100-singly_linked_list.py](./100-singly_linked_list.py)

### 8. Print Square instance
A class `Square` that defines a square based on `6-square.py`.

**File**: [101-square.py](./101-square.py)

### 9. Compare 2 square
A class `Square` that define a square based on `4-square.py`.

**File**: [102-square.py](./102-square.py)

### 10. ByteCode -> Python #5
Write the class `MagicClass` that does exactly the same as the following Python bytecode:

```
Disassembly of __init__:
 10           0 LOAD_CONST               1 (0)
              3 LOAD_FAST                0 (self)
              6 STORE_ATTR               0 (_MagicClass__radius)

 11           9 LOAD_GLOBAL              1 (type)
             12 LOAD_FAST                1 (radius)
             15 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             18 LOAD_GLOBAL              2 (int)
             21 COMPARE_OP               9 (is not)
             24 POP_JUMP_IF_FALSE       60
             27 LOAD_GLOBAL              1 (type)
             30 LOAD_FAST                1 (radius)
             33 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             36 LOAD_GLOBAL              3 (float)
             39 COMPARE_OP               9 (is not)
             42 POP_JUMP_IF_FALSE       60

 12          45 LOAD_GLOBAL              4 (TypeError)
             48 LOAD_CONST               2 ('radius must be a number')
             51 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             54 RAISE_VARARGS            1
             57 JUMP_FORWARD             0 (to 60)

 13     >>   60 LOAD_FAST                1 (radius)
             63 LOAD_FAST                0 (self)
             66 STORE_ATTR               0 (_MagicClass__radius)
             69 LOAD_CONST               3 (None)
             72 RETURN_VALUE

Disassembly of area:
 17           0 LOAD_FAST                0 (self)
              3 LOAD_ATTR                0 (_MagicClass__radius)
              6 LOAD_CONST               1 (2)
              9 BINARY_POWER
             10 LOAD_GLOBAL              1 (math)
             13 LOAD_ATTR                2 (pi)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE

Disassembly of circumference:
 21           0 LOAD_CONST               1 (2)
              3 LOAD_GLOBAL              0 (math)
              6 LOAD_ATTR                1 (pi)
              9 BINARY_MULTIPLY
             10 LOAD_FAST                0 (self)
             13 LOAD_ATTR                2 (_MagicClass__radius)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE
```