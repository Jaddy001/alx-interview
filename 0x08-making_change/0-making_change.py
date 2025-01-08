#!/usr/bin/python3
"""making change"""

def makeChange(coins, total):
    """ return the minimal change """
    if total <= 0:
        return 0

    coin.sort(reverse=True)
    num_change = 0
    sum_change = 0

    for i in coin:
        while sum_change < total:
            sum_change += 1
            num_change += 1
        if sum_change == total:
            return num_change
        sum_change -= 1
        num_change -= 1

    return -1

