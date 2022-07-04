#!/usr/bin/python3
def element_at(my_list, i):
    if i < 0:
        return (None)

    length = len(my_list)

    if i > length - 1:
        return (None)

    return(my_list[i])
