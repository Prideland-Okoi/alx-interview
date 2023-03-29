#!/usr/bin/python3
""" Function to find perimeter """


def island_perimeter(grid):
    """
    Input: List of Lists
    Returns: Perimeter of the island
    """
    count = 0
    row = len(grid)
    col = len(grid[0]) if row else 0

    for length in range(len(grid)):
        for breadth in range(len(grid[length])):

            islx = [(length - 1, breadth), (length, breadth - 1), (length, breadth + 1), (length + 1, breadth)]
            check = [1 if k[0] in range(row) and k[1] in range(col) else 0
                     for k in islx]

            if grid[length][breadth]:
                count += sum([1 if not r or not grid[k[0]][k[1]] else 0
                              for r, k in zip(check, islx)])

    return (count)
