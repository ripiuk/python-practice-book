"""
Problem:
    Write a function `group(list, size`) that take a list
    and splits into smaller lists of given size.

Solution:
    >>> import typing as typ
    >>> def group(list_: typ.List[typ.Any], size: int) -> typ.List[typ.Any]:
    ...     return [list_[pointer:pointer+size] for pointer in range(0, len(list_), size)]

    >>> group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
    [[1, 2, 3, 4], [5, 6, 7, 8], [9]]
"""
