#!/usr/bin/python3
# Prints all the names defined by the compiled module hidde_4.pyc

if __name__ == "__main__":

    import hidden_4

    for names in dir(hidde_4):
        if not names.startswith("__"):
            print("{:s}".format(names))
