#!/bin/bash
# Connect to the url, then get the Content-Length in the response header
sudo curl -sI '$1' | grep -i Content-Length | awk '{print $2}'
