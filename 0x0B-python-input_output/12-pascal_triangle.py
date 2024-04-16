#!/usr/bin/python3
"""Pascal Triangle."""


def pascal_triangle(n):
    """Represetn a pascal triangle of n size

    Return:
         list of lists of integers representing triangle.
    """
    if n <= 0:
        return []
    tri = [[1]]

    for i in range(n-1):
        row = [1]
        for j in range(i):
            val = tri[i][j] + tri[i][j+1]
            row.append(val)
        row.append(1)
        tri.append(row)

    return tri
