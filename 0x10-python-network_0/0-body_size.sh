#!/bin/bash
# Connect to the url, then get the Content-Length in the response header
sudo curl -s '$1' --include | grep -i Content-Length | awk '{print $2}'