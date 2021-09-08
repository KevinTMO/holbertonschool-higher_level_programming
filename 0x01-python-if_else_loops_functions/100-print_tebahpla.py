#!/usr/bin/python3
for alpha in range(ord('z'), ord('a') - 1, -1):
    if alpha % 2 == 1:
        print("{:c}".format(alpha - 32), end='')
    else:
        print(chr(alpha), end='')
