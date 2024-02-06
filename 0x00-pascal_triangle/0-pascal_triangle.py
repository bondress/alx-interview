#!/usr/bin/python3
"""This python script determines pascal's triangle for any number"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    tri = []

    # return (trianlgle if n <= 0)
    if n <= 0:
        return tri
    for i in range(n):
        tmp = []

        for j in range(i+1):
            if j == 0 or j == i:
                tmp.append(1)
            else:
                tmp.append(tri[i-1][j-1] + tri[i-1][j])
        tri.append(tmp)
    # print(tri)
    return tri
