#!/usr/bin/python3
'''Transpose 2d matrix in place'''


def rotate_2d_matrix(matrix: list[list[int]]) -> None:
    """Function to rotate matrix"""
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i] = matrix[i][::-1]
