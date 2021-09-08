#!/usr/bin/python3
# Print alphabet without q and e in lowercase
for alpha in range(ord('a'), ord('z') + 1):
    if alpha is not ord('e') and alpha is not ord('q'):
        # if alpha != ord('e') and alpha != ord('q') works too
        print("{:s}".format(chr(alpha)), end='')
