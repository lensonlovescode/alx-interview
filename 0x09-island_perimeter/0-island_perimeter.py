#!/usr/bin/python3
"""
The goal is to calculate the perimeter of a single island in a grid
where the grid is represented by a 2D array of integers
"""


def island_perimeter(grid):
    """
    calculates the perimeter of the island in the grid
    """
    num_rows = len(grid)
    num_cols = len(grid[0])
    perimeter = 0
    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == 1:
                perimeter += 4
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
    return perimeter
