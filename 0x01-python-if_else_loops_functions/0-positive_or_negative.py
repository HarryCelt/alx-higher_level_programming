#!/usr/bin/python3
import random as rd
num = rd.randint(-10, 10)
if num > 0:
    print('{:d} is positive'.format(num))
elif num == 0:
    print('{:d} is zero'.format(num))
else:
    print('{:d} is negative'.format(num))
