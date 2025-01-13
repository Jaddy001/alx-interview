#!/usr/bin/python3
"""
Module 0-pascal_triangle
Generates Pascal's Triangle up to a given number of rows.
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal’s Triangle.

    Args:
        n (int): Number of rows in Pascal's Triangle.

    Returns:
        List[List[int]]: Pascal's Triangle up to row n.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row

    for i in range(1, n):
        row = [1]  # Start each row with 1
        for j in range(1, i):
            # Add the two elements above the current position
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle

