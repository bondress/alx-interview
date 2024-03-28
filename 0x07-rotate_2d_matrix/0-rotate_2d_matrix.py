#!/usr/bin/python3
"""
This is th Rotate 2D Matrix Module
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise.
    """
    for i in range(int(len(matrix) / 2)):
        for j in range(i, (len(matrix) - i - 1)):
            n = (len(matrix) - 1 - j)
            tmp = matrix[i][j]
            matrix[i][j] = matrix[n][i]
            matrix[n][i] = matrix[(len(matrix) - i - 1)][n]
            matrix[(len(matrix) - i - 1)][n] = matrix[j][(len(matrix) - i - 1)]
            matrix[j][(len(matrix) - i - 1)] = tmp
