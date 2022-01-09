#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends
a request to the URL and displays the body of the response (decoded in utf-8).

- You have to manage urllib.error.HTTPError exceptions and print: Error
  code: followed by the HTTP status code
- You must use the packages urllib and sys
- You are not allowed to import other packages than urllib and sys
- You don’t need to check arguments passed to the script (number or type)
- You must use the with statement
"""


from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":

    urlPort = argv[1]
    response = Request(urlPort)

    try:
        with urlopen(response) as File:
            print(File.read().decode('utf-8'))

    except HTTPError as err:
        print('Error code: {}'.format(err.code))
