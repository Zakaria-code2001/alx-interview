#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    Returns an empty list if n <= 0
    """
    if n <= 0:
        return []
    box = []
    for i in range(n):
        if i == 0:
            box.append([1])
        else:
            new_row = [1]
            previous_row = box[-1]
            for j in range(1, len(previous_row)):
                new_row.append(previous_row[j] + previous_row[j - 1])
            new_row.append(1)
            box.append(new_row)

    return box
