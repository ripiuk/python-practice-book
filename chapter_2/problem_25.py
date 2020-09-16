"""
Problem:
    Python provides a built-in function `map` that applies a function
    to each element of a list. Provide an implementation for `map`
    using list comprehensions.

Solution:
    >>> import typing as typ
    >>> def map_(fn: typ.Callable, iterables: typ.Iterable) -> typ.List[typ.Any]:
    ...     return [fn(el) for el in iterables]

    >>> def square(x): return x * x
    >>> map_(square, range(5))
    [0, 1, 4, 9, 16]
    >>> map_(len, [[1, 2, 3], [1, 2]])
    [3, 2]
    >>> map_(lambda x: x ** 2, range(5))
    [0, 1, 4, 9, 16]
"""
