#!/usr/bin/python3
def print_last_digit(num):
    if num > 0:
        num = num % 10
    else:
        last_digit = num * -1
        num = last_digit % 10
    print(num, end="")
    return num
