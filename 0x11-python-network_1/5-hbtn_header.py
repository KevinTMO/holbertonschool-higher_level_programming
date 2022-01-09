#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays the
value of the variable X-Request-Id in the response header

- You must use the packages requests and sys
- You are not allow to import other packages than requests and sys
- The value of this variable is different for each request
- You don’t need to check script arguments (number and type)
"""


from requests import get
from sys import argv


if __name__ == '__main__':

    urlPort = argv[1]
    key = "X-Request-Id"
    response = get(urlPort).headers.get(key)
    print(response)
