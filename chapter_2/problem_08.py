"""
Problem:
    Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...].
    Write a function `cumulative_sum` to compute cumulative sum of a list.
    Does your implementation work for a list of strings?

Solution:
    >>> import typing as typ
    >>> from itertools import accumulate
    >>> def cumulative_sum(list_: typ.List[typ.Union[int, str]]) -> typ.List[typ.Union[int, str]]:
    ...     return list(accumulate(list_))

    >>> cumulative_sum([1, 2, 3, 4])
    [1, 3, 6, 10]
    >>> cumulative_sum([4, 3, 2, 1])
    [4, 7, 9, 10]
    >>> cumulative_sum(['a', 'b', 'c'])
    ['a', 'ab', 'abc']


    Native implementation without "cheating" with itertools.accumulate
    >>> def cumulative_sum_native(list_: typ.List[typ.Union[int, str]]) -> typ.List[typ.Union[int, str]]:
    ...     def accumulate_():
    ...         total = list_[0]
    ...         yield total
    ...         for el in list_[1:]:
    ...             total += el
    ...             yield total
    ...     return list(accumulate_())

    >>> cumulative_sum_native([1, 2, 3, 4])
    [1, 3, 6, 10]
    >>> cumulative_sum_native([4, 3, 2, 1])
    [4, 7, 9, 10]
    >>> cumulative_sum_native(['a', 'b', 'c'])
    ['a', 'ab', 'abc']
"""
