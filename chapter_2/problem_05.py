"""
Problem:
    Write a function `factorial` to compute factorial of a number.
    Can you use the `product` function defined in the previous example to compute factorial?

Solution:
    >>> from functools import reduce
    >>> import typing as typ
    >>> def product(list_: typ.Iterable[int]) -> int:
    ...     return reduce(lambda x, y: x * y, list_)
    >>> def factorial(num: int) -> int:
    ...     return product(range(1, num + 1))

    >>> factorial(4)
    24
    >>> factorial(5)
    120
"""
