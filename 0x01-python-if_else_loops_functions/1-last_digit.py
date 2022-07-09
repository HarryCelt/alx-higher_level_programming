#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
last_digit = abs(num) % 10
mess = "last digit of "
if num < 0:
    last_digit = -last_digit
else:
    last_digit = last_digit
if last_digit > 5:
    print("{}{} is {} and is greater than 5\
            ".format(mess, num, last_digit), end="")
elif last_digit == 0:
    print("{}{} is {} and is o".format(mess, num, last_digit))
else:
    print("{}{} is {} and is less than 6 and not 0\
            ".format(mess, num, last_digit))
