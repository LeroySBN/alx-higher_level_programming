# Python - Network #1
## Resources
* [HOWTO Fetch Internet Resources Using urllib Package](https://docs.python.org/3/howto/urllib2.html)
* [Quickstart with Requests package](https://requests.readthedocs.io/en/latest/)
* [Requests package](https://pypi.org/project/requests/)

## Tasks
### 0. What's my status? #0
Python script that fetches `https://alx-intranet.hbtn.io/status`
File: [0-hbtn_status.py](./0-hbtn_status.py)

### 1. Response header value #0
Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.

File: [1-hbtn_header.py](./1-hbtn_header.py)

### 2. POST an email #0
Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`)

File: [2-post_email.py]{./2-post_email.py)

### 3. Error code #0
Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`).
* You have to manage `urllib.error.HTTPError` exceptions and print: `Error code`: followed by the HTTP status code
* You must use the packages `urllib` and `sys`, no other packages should be imported

File: [3-error_code.py](./3-error_code.py)

### 4. What's my status? #1
Python script that fetches https://alx-intranet.hbtn.io/status
* You must use the package `requests`, no other packages should be imported

File: [4-hbtn_status.py](./4-hbtn_status.py)

### 5. Response header value #1
Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header
* You must use the packages `requests` and `sys`, no other packages should be imported

File: [5-hbtn_header.py](./5-hbtn_header.py)

### 6. POSTan email #1
Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
* The email must be sent in the variable `email`
* You must use the packages `requests` and `sys`, no other packages should be imported

File: [6-post_email.py](./6-post_email.py)

### 7. Error code #1
Python script that takes in a URL, sends a request to the URL and displays the body of the response.
* If the HTTP status code is greater than or equal to 400, print: `Error code`: followed by the value of the HTTP status code
* You must use the packages `requests` and `sys`, no other packages should be imported

File: [7-error_code.py](./ 7-error_code.py)

### 8. Search API
Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
* The letter must be sent in the variable `q`
* If no argument is given, set `q=""`
* If the response body is properly JSON formatted and not empty, display the `id` and `name` like this: `[<id>] <name>`
* Otherwise:
  * Display `Not a valid JSON if the JSON` is invalid
  * Display `No result` if the JSON is empty
* You must use the packages `requests` and `sys`, no other packages should be imported

File: [8-json_api.py](./8-json_api.py)

### 9. My GitHub!
Python script that takes your GitHub credentials (username and password) and uses the [GitHub API](https://docs.github.com/en/rest/users) to display your `id`
* You must use [Basic Authentication](https://docs.github.com/en/rest/overview/authenticating-to-the-rest-api?apiVersion=2022-11-28) with a [personal access token as password](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) to access to your information (only `read:user` permission is needed)
* The first argument will be your `username`
* The second argument will be your `password` (in your case, a [personal access token as password](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token))

File: [10-my_github.py](./10-my_github.py)

### 10. Time for an interview!
The Holberton School staff evaluates candidates applying for a back-end position with multiple technical challenges, like this one:
```
Please list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
```

Write a Python script that takes 2 arguments in order to solve this challenge.
* The first argument will be the `repository name`
* The second argument will be the `owner name`
* You must use the packages `requests` and `sys`, no other packages should be imported

File: [100-github_commits.py](./100-github_commits.py)
