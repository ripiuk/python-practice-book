"""
Problem:
    Write a function `cumulative_product` to compute cumulative product of a list of numbers.

Solution:
    >>> import typing as typ
    >>> from itertools import accumulate
    >>> import operator
    >>> def cumulative_product(list_: typ.List[typ.Union[int, str]]) -> typ.List[typ.Union[int, str]]:
    ...     return list(accumulate(list_, operator.mul))

    >>> cumulative_product([1, 2, 3, 4])
    [1, 2, 6, 24]
    >>> cumulative_product([4, 3, 2, 1])
    [4, 12, 24, 24]


    Native implementation without "cheating" with itertools.accumulate
    >>> def cumulative_product_native(list_: typ.List[typ.Union[int, str]]) -> typ.List[typ.Union[int, str]]:
    ...     def accumulate_():
    ...         total = list_[0]
    ...         yield total
    ...         for el in list_[1:]:
    ...             total *= el
    ...             yield total
    ...     return list(accumulate_())

    >>> cumulative_product_native([1, 2, 3, 4])
    [1, 2, 6, 24]
    >>> cumulative_product_native([4, 3, 2, 1])
    [4, 12, 24, 24]
"""
