#!/usr/bin/python3
# Print an alphabet using loops
for alpha in range(ord('a'), ord('z') + 1):
    print("{:s}".format(chr(alpha)), end='')
