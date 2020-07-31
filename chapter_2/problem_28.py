"""
Problem:
    Write a function `enumerate` that takes a list and returns a list
    of tuples containing `(index,item)` for each item in the list.

Solution:
    >>> import typing as typ
    >>> def enumerate_(iterable) -> typ.List[typ.Tuple[int, typ.Any]]:
    ...     return list(zip(range(len(iterable)), iterable))

    >>> enumerate_(["a", "b", "c"])
    [(0, 'a'), (1, 'b'), (2, 'c')]
    >>> for index, value in enumerate(["a", "b", "c"]):
    ...     print(index, value)
    0 a
    1 b
    2 c
"""
