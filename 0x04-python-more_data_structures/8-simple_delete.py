#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    try:
        del a_dictionary[key]
        return (a_dictionary)
    except keyError:
        return (a_dictionary)