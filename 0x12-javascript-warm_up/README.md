# JavaScript - warm up

[![js-semistandard-style](https://raw.githubusercontent.com/standard/semistandard/master/badge.svg)](https://github.com/standard/semistandard)

JavaScript is used for many things. Here, you will use JavaScript for 2 reasons:
* Scripting (same as we did with Python)
* Web front-end

![js](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/303/Javascript-535.png.jpeg)

## Resources
* [Writing JavaScript Code](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
* [Variables](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables)
* [Data Types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
* [Operators](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
* [Operator Precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence)
* [Controlling Program Flow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
* [Functions](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Functions)
* [Objects and Arrays and Intrinsic Objects](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
* [Module patterns](https://darrenderidder.github.io/talks/ModulePatterns/#/)
* [var, let and const](https://www.youtube.com/watch?v=sjyJBL5fkp8)
* [JavaScript Tutorial](https://www.youtube.com/watch?v=vZBCTc9zHtI)
* [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

***

## Tasks

### 0. First constant, first print
script that prints “JavaScript is amazing”:
* You must create a constant variable called `myVar` with the value “JavaScript is amazing”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

File: [0-javascript_is_amazing.js](./0-javascript_is_amazing.js)

### 1. 3 languages
script that prints 3 lines:
* The first line: “C is fun”
* The second line: “Python is cool”
* The third line: “JavaScript is amazing”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

File: [1-multi_languages.js](./1-multi_languages.js)

### 2. Arguments
script that prints a message depending of the number of arguments passed:
* If no arguments are passed to the script, print “No argument”
* If only one argument is passed to the script, print “Argument found”
* Otherwise, print “Arguments found”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

Reference: [process.argv](https://nodejs.org/api/process.html#process_process_argv)

File: [2-arguments.js](./2-arguments.js)

### 3. Value of my argument
script that prints the first argument passed to it:
* If no arguments are passed to the script, print “No argument”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You are not allowed to use `length`

File: [3-value_argument.js](./3-value_argument.js)

### 4.Create a sentence
script that prints two arguments passed to it, in the following format: “ is ”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

File: [4-concat.js](./4-concat.js)

### 5. An Integer
script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:

* If the argument can’t be converted to an integer, print “Not a number”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You are not allowed to use `try/catch`

File: [5-to_integer.js](./5-to_integer.js)

### 6. Loop to languages
script that prints 3 lines: (like `1-multi_languages.js`) but by using an array of string and a loop
* The first line: “C is fun”
* The second line: “Python is cool”
* The third line: “JavaScript is amazing”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You are not allowed to use any `if/else` statement
* You can use only one `console.log`
* You must use a loop (`while`, `for`, etc.)

File: [6-multi_languages_loop.js](./6-multi_languages_loop.js)

### 7. I love C
script that prints x times “C is fun”
* Where `x` is the first argument of the script
* If the first argument can’t be converted to an integer, print “Missing number of occurrences”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You can use only one `console.log`
* You must use a loop (`while`, `for`, etc.)

File: [7-multi_c.js](./7-multi_c.js)

### 8. Square
script that prints a square
* The first argument is the size of the square
* If the first argument can’t be converted to an integer, print “Missing size”
* You must use the character `X` to print the square
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You must use a loop (`while`, `for`, etc.)

File: [8-square.js](./8-square.js)

### 9. Add
script that prints the addition of 2 integers
* The first argument is the first integer
* The second argument is the second integer
* You have to define a function with this prototype: `function add(a, b)`
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

File: [9-add.js](./9-add.js)

### 10. Factorial
script that computes and prints a factorial
* The first argument is integer (argument can be cast as integer) used for computing the factorial
* Factorial of `NaN` is `1`
* You must do it recursively
* You must use a function
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

File: [10-factorial.js](./10-factorial.js)

### 11. Second biggest!
script that searches the second biggest integer in the list of arguments.
* You can assume all arguments can be converted to integer
* If no argument passed, print `0`
* If the number of arguments is 1, print `0`
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

File: [11-second_biggest.js](./11-second_biggest.js)

### 12. Object
Update this script to replace the value `12` with `89`:
* You are not allowed to use `var`

```
guillaume@ubuntu:~/0x12$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
guillaume@ubuntu:~/0x12$
```

File: [12-object.js](./12-object.js)

### 13. Add file
function that returns the addition of 2 integers.
* The function must be visible from outside
* The name of the function must be `add`
* You are not allowed to use `var`

[Tip](https://51elliot.blogspot.com/2012/01/simple-intro-to-nodejs-module-scope.html)

```
guillaume@ubuntu:~/0x12$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
guillaume@ubuntu:~/0x12$ ./13-main.js
8
guillaume@ubuntu:~/0x12$
```

File: [13-add.js](./13-add.js)

### 14. Const or not const
Write a file that modifies the value of myVar to 333

```
guillaume@ubuntu:~/0x12$ cat 100-main.js
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
guillaume@ubuntu:~/0x12$ ./100-main.js
333
guillaume@ubuntu:~/0x12$ 
```

File: [100-let_me_const.js](./100-let_me_const.js)

### 15. Call me Moby
function that executes `x` times a function.
* The function must be visible from outside
* Prototype: `function (x, theFunction`)
* You are not allowed to use `var`

```
guillaume@ubuntu:~/0x12$ cat 101-main.js
#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
guillaume@ubuntu:~/0x12$ ./101-main.js
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$
```

File: [101-call_me_moby.js](./101-call_me_moby.js)

### 16. Add me maybe
function that increments and calls a function.
* The function must be visible from outside
* Prototype: `function (number, theFunction)`
* You are not allowed to use `var`

```
guillaume@ubuntu:~/0x12$ cat 102-main.js
#!/usr/bin/node
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
guillaume@ubuntu:~/0x12$ ./102-main.js
New value: 5
guillaume@ubuntu:~/0x12$
```

File: [102-add_me_maybe.js](./102-add_me_maybe.js)

### 17. Increment object
Update this script by adding a new function `incr` that increments the integer `value`.
* You are not allowed to use `var`

```
guillaume@ubuntu:~/0x12$ cat 103-object_fct.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./103-object_fct.js 
{ type: 'object', value: 12 }
{ type: 'object', value: 13, incr: [Function] }
{ type: 'object', value: 14, incr: [Function] }
{ type: 'object', value: 15, incr: [Function] }
guillaume@ubuntu:~/0x12$
```

File: [103-object_fct.js](./103-object_fct.js)
