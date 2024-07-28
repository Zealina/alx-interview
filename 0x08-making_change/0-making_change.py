#!/usr/bin/python3
"""Coin chnage problem using greedy algorithm"""


def makeChange(coins, total):
    """Return the minimum amount of coins to make total"""
    if total <= 0 or not coins:
        return 0
    coins = sorted(coins, reverse=True)
    output = 0

    for coin in coins:
        if coin <= total:
            count = total // coin
            output += count
            total -= coin * count
        if total == 0:
            return output
    return -1 if total > 0 else output
