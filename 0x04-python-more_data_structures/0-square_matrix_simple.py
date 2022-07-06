#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    a = 0
    for i in matrix:
        new_matrix.append([])
        for j in matrix[a]:
            new_matrix[a].append(j**2)
        i += 1
    return (new_matrix)
