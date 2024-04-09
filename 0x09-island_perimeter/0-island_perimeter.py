#!/usr/bin/python3
"""This module defines the island perimeter finding function."""


def island_perimeter(grid):
    """This function returns the perimiter of an island.
    The grid represents water by 0 and land by 1.
    Args:
        grid (list): A list of list of integers representing an island.
    Returns:
        The perimeter of the island defined in grid.
    """
    width = len(grid[0])
    height = len(grid)
    edges = 0
    size = 0

    for n in range(height):
        for o in range(width):
            if grid[n][o] == 1:
                size += 1
                if (o > 0 and grid[n][o - 1] == 1):
                    edges += 1
                if (n > 0 and grid[n - 1][o] == 1):
                    edges += 1
    return size * 4 - edges * 2
