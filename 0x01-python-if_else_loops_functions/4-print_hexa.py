#!/usr/bin/python3
# Prints number in decimal and hexadecimal
for number in range(0, 98 + 1):
    print("{:d} = {:s}".format(number, hex(number)))
