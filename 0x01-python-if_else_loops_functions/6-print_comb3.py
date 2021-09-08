#!/usr/bin/python3
# Print any posible combination without reapeting same digits from before
for number in range(0, 9 + 1):
    for number2 in range(0, 9 + 1):
        if number < number2:
            print("{:d}{:d}".format(number, number2), end='')
            if number is not 8:
                print(", ", end="")
print('')
