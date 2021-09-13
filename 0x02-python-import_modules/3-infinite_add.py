#!/usr/bin/python3
# Infinite addition. Print the addition of all arguments.

if __name__ == "__main__":

    from sys import argv

    print(sum(map(int, argv[1:])))
