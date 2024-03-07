#!/usr/bin/python3
"""Generate Pascal's Triangle"""


def pascal_triangle(n):
    """Generate Pascal's Triangle"""
    result = []
    for i in range(0, n):
        val = 1
        row = []
        for j in range(0, i):
            row.append(val)
            val = val * (i - j) // (j + 1)
        row.append(1)
        result.append(row)
    return result
