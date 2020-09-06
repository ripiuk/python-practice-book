"""
Problem:
    Implement a function `izip` that works like `itertools.izip`
    (equivalent to Python3 built-in `zip` function).

Solution:
    >>> import typing as typ
    >>> def zip_(*iterables: typ.Iterable[typ.Any]) -> typ.Iterator[typ.Tuple[typ.Any, ...]]:
    ...     iterators = [iter(it) for it in iterables]
    ...     while iterators:
    ...         result = []
    ...         for it in iterators:
    ...             try:
    ...                 value = next(it)
    ...                 result.append(value)
    ...             except StopIteration:
    ...                 return
    ...         yield tuple(result)

    >>> list(zip_(['a', 'b', 'c'], [1, 2, 3]))
    [('a', 1), ('b', 2), ('c', 3)]

    >>> list(zip_(['a', 'b', 'c'], [1, 2, 3], 'txt'))
    [('a', 1, 't'), ('b', 2, 'x'), ('c', 3, 't')]

    >>> for x, y in zip_(['a', 'b', 'c'], [1, 2, 3]):
    ...     print(x, y)
    a 1
    b 2
    c 3
"""
