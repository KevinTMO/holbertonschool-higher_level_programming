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

    with get('https://intranet.hbtn.io/status') as File:
        print('Body response:')
        print('    - type: {}'.format(type(File.text)))
        print('    - content: {}'.format(File.text))
