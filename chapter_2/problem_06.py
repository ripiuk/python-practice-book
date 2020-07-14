"""
Problem:
    Write a function `reverse` to reverse a list.
    Can you do this without using list slicing and build-in reverse function?

Solution:
    >>> import typing as typ
    >>> def reverse(list_: typ.List[typ.Any]) -> typ.List[typ.Any]:
    ...     return [list_[i] for i in range(len(list_) - 1, -1, -1)]

    >>> reverse([1, 2, 3, 4])
    [4, 3, 2, 1]
    >>> reverse(reverse([1, 2, 3, 4]))
    [1, 2, 3, 4]
"""
