#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
and displays the body of the response.

- If the HTTP status code is greater than or equal to 400, print: Error code:
  followed by the value of the HTTP status code
- You must use the packages requests and sys
- You are not allowed to import packages other than requests and sys
- You don’t need to check arguments passed to the script (number or type)
"""


from requests import get
from sys import argv


if __name__ == "__main__":

    urlPort = argv[1]
    response = get(urlPort)
    code = response.status_code

    if code < 400:
        print(response.text)

    else:
        print("Error code: {}".format(code))
