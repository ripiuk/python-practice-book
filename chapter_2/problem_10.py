"""
Problem:
    Write a function `unique` to find all the unique elements of a list.

Solution:
    >>> import typing as typ
    >>> def unique(list_: typ.List[typ.Any]) -> typ.List[typ.Any]:
    ...     return list(set(list_))

    >>> unique([1, 2, 1, 3, 2, 5])
    [1, 2, 3, 5]
"""
