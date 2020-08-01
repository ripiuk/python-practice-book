"""
Problem:
    Write a function `invertdict` to interchange keys and values in a dictionary.
    For simplicity, assume that all values are unique.

Solution:
    >>> def invertdict(dict_: dict) -> dict:
    ...     return {v: k for k, v in dict_.items()}

    >>> invertdict({'x': 1, 'y': 2, 'z': 3})
    {1: 'x', 2: 'y', 3: 'z'}
    >>> invertdict({'c': 10, 'k': 10, 'z': 9})
    {10: 'k', 9: 'z'}
"""
