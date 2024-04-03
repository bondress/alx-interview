#!/usr/bin/python3
"""
This module returns the
fewest number of coins needed to
meet a given amount total
"""


def makeChange(coins, total):
    """This is the makeChange function."""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    output = 0
    for coin in coins:
        if total <= 0:
            break
        tmp = total // coin
        output += tmp
        total -= (tmp * coin)
    if total != 0:
        return -1
    return output
