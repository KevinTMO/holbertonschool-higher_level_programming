#!/bin/bash
# GET request on an URL && if redirect then follow it with -L
curl -Ls "$1"
