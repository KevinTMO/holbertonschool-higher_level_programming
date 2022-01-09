#!/bin/bash
# Connect to the url, then get the Content-Length in the response header
curl -si 0.0.0.0:5000 | grep -i Content-Length | cut -d " " -f 2
