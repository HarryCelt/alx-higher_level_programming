#!/usr/bin/python3
import random as rd
num = rd.randint(-10000, 10000)
last_digit = abs(num) % 10
mess = "last digit of "
if num < 0:
    last_digit = -last_digit
print("{}{} is {} and is ".format(mess, num, last_digit), end="")
if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
