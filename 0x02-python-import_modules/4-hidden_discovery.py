#!/usr/bin/python3
# Prints all the names defined by the compiled module hidde_4.pyc

if __name__ == "__main__":

    import hidden_4

    names = dir(hidden_4)

    for getNames in names:
        if getNames[0] != '_' and getNames[1] != '_':
            print("{:s}".format(getNames))

#    for names in dir(hidden_4):
#        if not names.startswith("__"):
#            print("{:s}".format(names))
