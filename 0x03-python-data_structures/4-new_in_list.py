#!/usr/bin/python3
def new_in_list(my_list, i, j):
    length = len(my_list)

    new_list = my_list[:]

    if 0 <= i < length:
        new_list[i] = j

    return (new_list)
