#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id

- You must use Basic Authentication with a
  personal access token as password to access to your information
  (only read:user permission is needed)
- The first argument will be your username
- The second argument will be your password
  (in your case, a personal access token as password)
- You must use the package requests and sys
- You are not allowed to import packages other than requests and sys
- You don’t need to check arguments passed to the script (number or type)
"""


from requests import get
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":

    url = "https://api.github.com/user"
    user = argv[1]
    passwd = argv[2]
    response = get(url, auth=HTTPBasicAuth(user, passwd))

    print(response.json().get('id'))
