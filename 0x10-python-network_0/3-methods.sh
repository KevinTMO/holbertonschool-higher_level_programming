#!/bin/bash
# Get all the methods available for route_4
curl -sI "$1" | grep -i Allow | cut -d " " -f 2-
