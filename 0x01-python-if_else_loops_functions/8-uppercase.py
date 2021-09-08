#!/usr/bin/python3
# Turn lowercase charcaters into uppercase


def uppercase(str):
    for char in str:
        if char.islower():
            print(chr(ord(char) - 32), end="")
        else:
            print(chr(ord(char)), end="")
    print("")
