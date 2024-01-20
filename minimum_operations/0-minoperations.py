#!/usr/bin/python3
"""calculates the fewest number of operations to result in n H chars"""


def minOperations(n):
    """Minimum Operations"""
    if n <= 1:
        return 0

    x = 2
    result = 0
    while x <= n:
        if n % x == 0:
            result += x
            n = n / x
        else:
            x += 1
    return result
