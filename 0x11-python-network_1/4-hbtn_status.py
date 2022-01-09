#!/usr/bin/python3
"""
Write a Python script that fetches https://intranet.hbtn.io/status

- You must use the package requests
- You are not allow to import packages other than requests
- The body of the response must be display like the following example
  (tabulation before -)
"""


from requests import get


if __name__ == '__main__':

    response = get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(response.text)))
    print('\t- content: {}'.format(response.text))
