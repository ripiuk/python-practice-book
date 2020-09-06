"""
Problem:
    The built-in function `enumerate` takes an iteratable and returns
    an iterator over pairs (index, value) for each value in the source.

Solution:
    >>> import typing as typ
    >>> from itertools import count
    >>> def enumerate_(elements: typ.Iterable[typ.Any]) -> typ.Iterator[typ.Tuple[int, typ.Any]]:
    ...     yield from zip(count(), elements)

    >>> list(enumerate_(["a", "b", "c"]))
    [(0, 'a'), (1, 'b'), (2, 'c')]

    >>> for i, c in enumerate_(["a", "b", "c"]):
    ...     print(i, c)
    ...
    0 a
    1 b
    2 c
"""
