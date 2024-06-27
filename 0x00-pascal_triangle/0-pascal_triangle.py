#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    box = []
    value = [1]
    if n <= 0:
        return []
    else:
        for i in range(n):
            if i == 0:
                box.append(value)
                print(value)
            else:
                new_row = [1]
                previous_row = box[-1]
                for j in range(1, len(previous_row)):
                    result = previous_row[j] + previous_row[j - 1]
                    new_row.append(result)
                new_row.append(1)
                box.append(new_row)
                print(new_row)
    
        return box


pascal_triangle(5)