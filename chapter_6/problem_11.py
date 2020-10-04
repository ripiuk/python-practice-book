"""
Problem:
    Write a function `vectorize` which takes a function `f` and return a new
    function, which takes a list as argument and calls `f` for every element
    and returns the result as a list.
"""

import typing as typ
from functools import wraps


def vectorize(fn: typ.Callable) -> typ.Callable:
    """Decorator that takes iterable object as an argument
    and calls needed function for every element

    Tests:
        >>> vectorize(lambda x: x * x)([1, 2, 3])
        [1, 4, 9]
        >>> vectorize(len)(["hello", "world"])
        [5, 5]
        >>> vectorize(len)([[1, 2], [2, 3, 4]])
        [2, 3]
        >>> vectorize(ord)('abcd')
        [97, 98, 99, 100]

    :param fn: function
    :return: decorated function
    """
    @wraps(fn)
    def wrap(iterable: typ.Iterable[typ.Any]) \
            -> typ.List[typ.Any]:
        return [fn(el) for el in iterable]
    return wrap
