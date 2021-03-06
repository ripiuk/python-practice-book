"""
Problem:
    Implement a function `product`, to compute product of a list of numbers.

Solution:
    >>> import typing as typ
    >>> from functools import reduce
    >>> def product(list_: typ.List[int]) -> int:
    ...     return reduce(lambda x, y: x * y, list_)

    >>> product([1, 2, 3])
    6
    >>> product([2, 5, 10])
    100
"""
