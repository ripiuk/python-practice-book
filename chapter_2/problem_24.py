"""
Problem:
    Provide an implementation for `zip` function using list comprehensions.

Solution:
    >>> import typing as typ
    >>> def zip_(*args: typ.List) -> typ.List[typ.Tuple]:
    ...     return [tuple(list_[i] for list_ in args) for i in range(min(map(len, args)))]

    >>> zip_([1, 2, 3], ['a', 'b', 'c'])
    [(1, 'a'), (2, 'b'), (3, 'c')]
    >>> zip_([1, 2, 3], ['a', 'b', 'c'], [10, 11])
    [(1, 'a', 10), (2, 'b', 11)]
"""
