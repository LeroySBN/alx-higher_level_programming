# More Classes and Objects
## Resources
### read
* [Object Oriented Programming](https://python.swaroopch.com/oop.html)
* [More Object Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php)
* [Class vs Instance Attributes](https://python-course.eu/oop/class-instance-attributes.php)
* [Properties vs Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
* [str vs repr](https://shipit.dev/posts/python-str-vs-repr.html)
### watch
* [classmethods and staticmethods](https://www.youtube.com/watch?v=rq8cL2XMM5M)

## Tasks
### 0. Simple rectangle
Empty class `Rectangle` that defines a rectangle.

**File**: [0-rectangle.py](./0-rectangle.py)

### 1. Real definition of a rectangle

Class `Rectangle` that further defines a rectangle (based on `0-rectangle.py`)

**File**: [1-rectangle.py](./1-rectangle.py)

### 2. Area and Perimeter

Class `Rectangle` that further defines a rectangle (based on `1-rectangle.py`)

**File**: [2-rectangle.py](./2-rectangle.py)

### 3. String representation

Class `Rectangle` that further defines a rectangle (based on `2-rectangle.py`)

**File**: [3-rectangle.py](./3-rectangle.py)

### 4. Eval is magic

Class `Rectangle` that further defines a rectangle (based on `3-rectangle.py`)

**File**: [4-rectangle.py](./4-rectangle.py)

### 5. Detect instance deletion

Class `Rectangle` that further defines a rectangle (based on `4-rectangle.py`)

**File**: [5-rectangle.py](./5-rectangle.py)

### 6. How many instances

Class `Rectangle` that further defines a rectangle (based on `5-rectangle.py`)

**File**: [6-rectangle.py](./6-rectangle.py)

### 7. Change representation

Class `Rectangle` that further defines a rectangle (based on `6-rectangle.py`)

**File**: [7-rectangle.py](./7-rectangle.py)

### 8. Compare rectangles

Class `Rectangle` that further defines a rectangle (based on `7-rectangle.py`)

**File**: [8-rectangle.py](./8-rectangle.py)

### 9. A square is a rectangle

Class `Rectangle` that further defines a rectangle (based on `8-rectangle.py`)

**File**: [9-rectangle.py](./9-rectangle.py)

### 10. N queens

![nqueens](http://www.crestbook.com/files/Judit-photo1_602x433.jpg)

The N queens puzzle is the challenge of placing N non-attacking queens on a NxN chessboard. For this task we write a program that solves the N queens problem.

* Usage: `nqueens N`: If the user called the program with the wrong number of arguments, prints `Usage: nqueens N`, followed by a new line, and then exits with the status `1`
* where N must be an integer greater or equal to 4: If `N is not an integer`, print N must be a number, followed by a new line, and exit with the status `1`. If N is smaller than `4`, print `N must be at least 4`, followed by a new line, and exit with the status `1`
* The program should print every possible solution to the problem: One solution per line

Read: [Queeen](https://en.wikipedia.org/wiki/Queen_%28chess%29), [Backtracking](https://en.wikipedia.org/wiki/Backtracking)

**File**: [101-nqueens.py](./101-nqueens.py)