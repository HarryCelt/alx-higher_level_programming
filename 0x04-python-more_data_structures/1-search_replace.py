#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    a = 0
    for i in my_list:
        if i is search:
            new_list[a] = replace
        a += 1
    return (new_list)
