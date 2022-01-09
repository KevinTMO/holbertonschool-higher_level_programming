#!/bin/bash
# Sending two variables and requesting a POST
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
