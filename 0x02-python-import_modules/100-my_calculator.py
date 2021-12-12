#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

        op = ['+', '-', '*', '/']

        if argv[2] not in op:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

            a = int(argv[1])
            b = int(argv[3])
            opr = str(argv[2])

            if opr == '+':
                print("{} {} {} = {}".format(a, opr, b, add(a, b)))

            if opr == '-':
                print("{} {} {} = {}".format(a, opr, b, sub(a, b)))

            if opr == '*':
                print("{} {} {} = {}".format(a, opr, b, mul(a, b)))

            if opr == '/':
                print("{} {} {} = {}".format(a, opr, b, div(a, b)))
