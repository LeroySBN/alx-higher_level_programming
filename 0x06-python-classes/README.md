# Classes and Objects
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

``