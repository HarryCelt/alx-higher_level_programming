#!/usr/bin/python3
def replace_in_list(my_list, i, j):
    if i < 0:
        return (my_list)

    length = len(my_list)

    if i > length - 1:
        return (my_list)

    my_list[i] = j

    return (my_list)
