#!/usr/bin/python3
# Print numbers from 0 to 99
#for number in range(0, 99 + 1):
#    print("{:02d}".format(number), end="")
#    if number is not 99:
#        print(", ", end='')
#print("")
print (", ".join("{:02d}".format(number) for number in range(0, 99 + 1)))
# Using .join will add a separator between each iterable item
