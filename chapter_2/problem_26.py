"""
Problem:
    Python provides a built-in function `filter(f, a)` that returns
    items of the list `a` for which `f(item)` returns true.
    Provide an implementation for `filter` using list comprehensions.

Solution:
    >>> import typing as typ
    >>> def filter_(fn: typ.Callable, args: typ.Iterable) -> typ.List[typ.Any]:
    ...     return [el for el in args if fn(el)]

    >>> def even(x): return x %2 == 0
    >>> filter_(even, range(10))
    [0, 2, 4, 6, 8]
    >>> filter_(lambda x: 8 > x > 3, range(10))
    [4, 5, 6, 7]
"""
