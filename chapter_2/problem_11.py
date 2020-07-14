"""
Problem:
    Write a function `dups` to find all duplicates in the list.

Solution:
    >>> import typing as typ
    >>> from collections import Counter
    >>> def dups(list_: typ.List[typ.Any]) -> typ.List[typ.Any]:
    ...     return [el for el, count in Counter(list_).items() if count > 1]

    >>> dups([1, 2, 1, 3, 2, 5])
    [1, 2]
    >>> dups([1, 2, 3])
    []
"""
