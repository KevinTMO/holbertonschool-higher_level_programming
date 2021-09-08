#!/usr/bin/python3
# Check if characters are lower or not and return true or false


def islower(c):
    for alpha in range(ord('a'), ord('z') + 1):
        if ord(c) == alpha:
            return True
    return False
