"""
Problem:
    Write a function `count_change` to count the number of ways to change
    any given amount. Available coins are also passed as argument to the function.
"""

import typing as typ


def count_change(amount: int, coins: typ.List[int]) -> int:
    """Counts how many different ways you can make change for
    an amount of money, given an array of coin denominations.

    For example, there are 3 ways to give change for 4
    if you have coins with denomination 1 and 2:
        1+1+1+1, 1+1+2, 2+2.
    The order of coins does not matter:
        1+1+2 == 2+1+1
    Also, assume that you have an infinite ammount of coins.

    Tests:
        >>> count_change(10, [1, 5])
        3
        >>> count_change(10, [1, 2])
        6
        >>> count_change(100, [1, 5, 10, 25, 50])
        292
        >>> count_change(4, [1, 2])
        3
        >>> count_change(10, [5, 2, 3])
        4
        >>> count_change(11, [5, 7])
        0

    :param amount: given amount of money
    :param coins: array of unique denominations for the coins
    :return: number of ways to make change for given amount of money
    """
    if amount == 0:
        return 1
    elif amount < 0 or len(coins) == 0:
        return 0
    return count_change(
        amount=amount - coins[0],
        coins=coins,
    ) + count_change(
        amount=amount,
        coins=coins[1:],
    )
