# JavaScript - Web scraping
## Resources
* [Working with JSON data](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)
* [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://medium.com/@vietkieutie/the-workflow-of-accessing-the-attributes-of-a-simply-created-json-object-82a5b33e2319)
* [request module](https://github.com/request/request)
* [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

## More Info
### Install Node 10
```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```
### Install semi-standard
[Documentation](https://github.com/standard/semistandard)
`$ sudo npm install semistandard --global`

### Install request module and use it
[Documentation](https://github.com/request/request)
```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```
>***Notes***: *Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).*

## Tasks
### 0. Readme
a script that reads and prints the content of a file.
* The first argument is the file path
* The content of the file must be read in `utf-8`
* If an error occurred during the reading, print the error object
File: [0-readme.js](./0-readme.js)

### 1. Write me
a script that writes a string to a file.
* The first argument is the file path
* The second argument is the string to write
* The content of the file must be written in `utf-8`
* If an error occurred during while writing, print the error object

File: [1-writeme.js](./1-writeme.js)

### 2. Status code
a script that display the status code of a `GET` request.
* The first argument is the URL to request (`GET`)
* The status code must be printed like this: `code: <status code>`
* You must use the module `request`

File: [2-statuscode.js](./2-statuscode.js)

### 3. Star wars movie title
a script that prints the title of a Star Wars movie where the episode number matches a given integer.
* The first argument is the movie ID
* You must use the [Star wars API](https://swapi-api.alx-tools.com/) with the endpoint `https://swapi-api.alx-tools.com/api/films/:id`
* You must use the module `request`

File: [3-starwars_title.js](./3-starwars_title.js)

### 4. Star wars Wedge Antilles
a script that prints the number of movies where the character “Wedge Antilles” is present.
* The first argument is the API URL of the [Star wars API](https://swapi-api.alx-tools.com/): `https://swapi-api.alx-tools.com/api/films/`
* Wedge Antilles is character ID `18` - your script **must** use this ID for filtering the result of the API
* You must use the module `request`

File: [4-starwars_count.js](./4-starwars_count.js)

### 5. Loripsum
a script that gets the contents of a webpage and stores it in a file.
* The first argument is the URL to request
* The second argument the file path to store the body response
* The file must be UTF-8 encoded
* You must use the module `request`

File: [5-request_store.js](./5-request_store.js)

### 6. How many completed?
a script that computes the number of tasks completed by user id.
* The first argument is the API URL: `https://jsonplaceholder.typicode.com/todos`
* Only print users with completed task
* You must use the module `request`

File: [6-completed_tasks.js](./6-completed_tasks.js)

### 7. Who was playing in this movie?
a script that prints all characters of a Star Wars movie:
* The first argument is the Movie ID - example: `3` = “Return of the Jedi”
* Display one character name by line
* You must use the [Star wars API](https://swapi-api.alx-tools.com/)
* You must use the module `request`

File: [100-starwars_characters.js](./100-starwars_characters.js)

### 8. Right order
a script that prints all characters of a Star Wars movie:
* The first argument is the Movie ID - example: `3` = “Return of the Jedi”
* Display one character name by line **in the same order of the list “characters” in the** `/films/` **response**
* You must use the [Star wars API](https://swapi-api.alx-tools.com/)
* You must use the module `request`

File: [101-starwars_characters.js](./101-starwars_characters.js)
