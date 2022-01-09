#!/usr/bin/python3
# Connect to the url, then get the Content-Length in the response header
# curl -s silence any error when connecting to the url 0.0.0.0:5000
# grep option -i looks matches even if they got upper or lowercase in them.
# awk will print the second column after grep match

curl -s '$1' --include | grep -i Content_Length |  awk '{print $2}'
