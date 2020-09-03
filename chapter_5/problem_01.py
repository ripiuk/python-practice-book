"""
Problem:
    Write an iterator class `reverse_iter`, that takes a list and iterates
    it from the reverse direction.

Solution:
    >>> import typing as typ
    >>> class ReverseIter:
    ...     def __init__(self, elements: typ.Iterable[typ.Any]):
    ...         self.elements = elements
    ...         self._i = len(elements) - 1
    ...
    ...     def __iter__(self):
    ...         return self
    ...
    ...     def __next__(self):
    ...         if self._i < 0:
    ...             raise StopIteration
    ...         self._i -= 1
    ...         return self.elements[self._i + 1]

    >>> it = ReverseIter([1, 2, 3, 4])
    >>> next(it)
    4
    >>> next(it)
    3
    >>> next(it)
    2
    >>> next(it)
    1
    >>> next(it)
    Traceback (most recent call last):
    ...
    StopIteration

    >>> it = ReverseIter('abc')
    >>> next(it)
    'c'
    >>> next(it)
    'b'
    >>> next(it)
    'a'
    >>> next(it)
    Traceback (most recent call last):
    ...
    StopIteration
"""
