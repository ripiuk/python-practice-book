"""
Problem:
    Write a function `array` to create an 2-dimensional array.
    The function should take both dimensions as arguments.
    Value of each element can be initialized to None:

Solution:
    >>> import typing as typ
    >>> def array(n: int, m: int) -> typ.List[typ.List[None]]:
    ...     return [[None for _ in range(m)] for _ in range(n)]

    >>> a = array(2, 3)
    >>> a
    [[None, None, None], [None, None, None]]
    >>> a[0][0] = 5
    >>> a
    [[5, None, None], [None, None, None]]
"""
