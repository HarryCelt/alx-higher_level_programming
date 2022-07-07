#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDict = {}
    for i in a_dictionary:
        newValue = (a_dictionary.get(i)) * 2
        newDict.update({i: newValue})
        return (newDict)
