"""
Problem:
    Python has a built-in function `sum` to find sum of all elements of a list.
    Provide an implementation for `sum`.

Solution:
    >>> import typing as typ
    >>> from functools import reduce
    >>> def sum_(list_: typ.List[int]) -> int:
    ...     return reduce(lambda x, y: x + y, list_)

    >>> sum_([1, 2, 3])
    6
"""
