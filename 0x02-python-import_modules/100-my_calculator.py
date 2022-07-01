#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-mycalculator.py <a> <operator> <b>")
        quit(1)
    a = int(argv[1])
    b = int(argv[3])
    operators = ["+", "-", "*", "/"]
    from calculator_1 import add, sub, mul, div
    functions = [add, sub, mul, div]
    for i, j in enumerate(operators):
        if argv[2] == j:
            print("{} {} {} = {}".format(a, j, b, functions[i](a, b)))
            break
        else:
            print("Unknown operator! Available operators are: +, -,  *, and /")
            quit(1)
