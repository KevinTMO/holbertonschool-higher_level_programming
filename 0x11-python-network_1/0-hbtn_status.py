#!/usr/bin/python3
"""
Write a Python script that fetches https://intranet.hbtn.io/status

- You must use the package urllib
- You are not allowed to import any packages other than urllib
- The body of the response must be displayed
  like the following example (tabulation before -)
- You must use a with statement
"""


if __name__ == '__main__':

    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as File:
        html = File.read()
        print('Body response:')
        print('    - type: {}'.format(type(html)))
        print('    - content: {}'.format(html))
        print('    - utf8 content: {}'.format(html.decode('utf-8')))
