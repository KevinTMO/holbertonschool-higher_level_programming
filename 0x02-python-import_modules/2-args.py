#!/usr/bin/python3
# Import argv to iterate arguments

if __name__ == "__main__":

    from sys import argv

    input_usr = argv[1:]
    input_size = len(input_usr)

    print("{:d} {:s}{:s}".format(input_size, "arguments" if input_size != 1
                                 else "argument", "." if input_size == 0
                                 else ":"))

    for index_args, args in enumerate(input_usr):
        print("{:d}: {:s}".format(index_args + 1, args))
