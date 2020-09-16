"""
Problem:
    Write a function `treemap` to map a function over nested list.

Solution:
    >>> import typing as typ
    >>> from collections.abc import Iterable

    >>> def tree_map(func: typ.Callable, iterables: typ.Iterable[typ.Any]) -> typ.List[typ.Any]:
    ...      return [
    ...         tree_map(func, el)
    ...         if isinstance(el, Iterable) and not isinstance(el, (str, bytes))
    ...         else func(el)
    ...         for el in iterables
    ...     ]

    >>> tree_map(lambda x: x*x, [1, 2, [3, 4, [5]]])
    [1, 4, [9, 16, [25]]]

    >>> tree_map(lambda x: x**2, (2, (3, (4, (5, (6, ), 7), 8), 9), 10))
    [4, [9, [16, [25, [36], 49], 64], 81], 100]

    >>> tree_map(ord, 'test text')
    [116, 101, 115, 116, 32, 116, 101, 120, 116]
"""
