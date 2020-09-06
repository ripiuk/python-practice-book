"""
Problem:
    Write a function `peep`, that takes an iterator as argument
    and returns the first element and an equivalent iterator.

Solution:
    >>> import typing as typ
    >>> from itertools import chain
    >>> def peep(elements: typ.Iterator[typ.Any]) -> typ.Tuple[typ.Any, typ.Iterator[typ.Any]]:
    ...     return (first_element := next(elements)), chain([first_element], elements)

    >>> it = iter(range(5))
    >>> x, it1 = peep(it)
    >>> print(x, list(it1))
    0 [0, 1, 2, 3, 4]
"""
