#!/usr/bin/python3
# Turn lowercase charcaters into uppercase


def uppercase(str):
    for char in str:
        asci = ord(char)
        if char.islower():
            asci = asci - 32
        print("{:c}".format(asci), end="")
    print("")
