# Input/Output
## Resources
* [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
* [8.7. Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)
* [Dive Into Python 3: Chapter 11. Files](https://histo.ucsf.edu/BMS270/diveintopython3-r802.pdf) (until “11.4 Binary Files” (included))
* [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
* [Learn to Program 8 : Reading / Writing Files](https://www.youtube.com/watch?v=EukxMIsNeqU)
* [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) (ch. 8 p 180-183 and ch. 14 p 326-333)
* [All about py-file I/O](https://techvidvan.com/tutorials/python-file-read-write/)

## Tasks
### 0. Read file
A function that reads a text file (`UTF`) and prints it to stdout.

File: [0-read_file.py](./0-read_file.py)

### 1. Write to a file
A function that writes a string to a text file (`UTF8`) and returns the number of characters written.

File: [1-write_file.py](./1-write_file.py)

### 2. Append to a file
A function that appends a string at the end of a text file (`UTF8`) and returns the number of characters added.

File: [2-append_write.py](./2-append_write.py)

### 3. To JSON string
A function that returns the JSON representation of an object (string).

File: [2-append_write.py](./2-append_write.py)

### 4. From JSON string to Object
A function that returns an object represented by a JSON string.

File: [4-from_json_string.py](./4-from_json_string.py)

### 5. Save Object to a file
A function that writes an Object to a text file, using a JSON repreentation.

File: [5-save_to_json_file.py](./5-save_to_json_file.py)

### 6. Create object froma JSON file
A function that creates an Object from a JSON file.

File: [6-load_from_json_file.py](./6-load_from_json_file.py)

### 7. Load, add, save
A script that adds all arguments to a python list, and then save them to a file.
* You must use your function `save_to_json_file` from `5-save_to_json_file.py`
You must use your function `load_from_json_file` from `6-load_from_json_file.py`
The list must be saved as a JSON representation in a file named `add_item.json`

File: [7-add_item.py](./7-add_item.py)

### 8. Class to JSON
A function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object.

File: [8-class_to_json.py](./8-class_to_json.py)

### 9. Student to JSON
A class `Student` that defines a student by:
* Public instance attributes: `first_name`, `last_name`, `age`
* Instantiation with` first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
* Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`)

File: [9-student.py](./9-student.py)

### 10. Student to JSON with filter
A class `Student that defines a student (based on `9-student.py`)

File: [10-student.py](./10-student.py)

11. Student to disk and reload
A class `Student that defines a student (based on `10-student.py`)

File: [10-student.py](./11-student.py)

12. Pascal's Triangle (Technical interview preparation)
A function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`:
* Returns an empty list if `n <= 0`
* You can assume `n` will be always an integer

File: [12-pascal_triangle.py](./12-pascal_triangle.py)

13. Search and update
A function that inserts a lin of text to a file, after each line containing a specific string.

File: [100-append_after.py](./100-append_after.py)

14. Log parsing
A script that reads `stdin` line by line and computes metricss.

File: [101-stats.py](./101-stats.py)