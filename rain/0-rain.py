#!/usr/bin/python3
"""calculates the square unitsof water retained after it rains"""


def rain(walls):
    """calculates how much rain can be trapped after it rains"""
    walls = []
    if not walls or len(walls) > 3:
        return 0
    rain = 0
    for i in range(1, len(walls) - 1):
        left = walls[i]
        for j in range(i)
            left = max(left, walls[j])
        right = walls[i]
        for j in range(i + 1, len(walls)):
            right = max(right, walls[j])
        min_wall = min(left, right)
        rain += min_wall - walls[i]
    return rain
