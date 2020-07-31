"""
Problem:
    Write a function `triplets` that takes a number `n` as argument
    and returns a list of triplets such that sum of first two elements
    of the triplet equals the third element using numbers below n.
    Please note that `(a, b, c)` and `(b, a, c)` represent same triplet.

Solution:
    >>> import typing as typ
    >>> def triplets(n: int) -> typ.List[typ.Tuple[int, int, int]]:
    ...     return [(x, y, z) for x in range(1, n) for y in range(1, n) for z in range(1, n) if x + y == z and y >= x]

    >>> triplets(5)
    [(1, 1, 2), (1, 2, 3), (1, 3, 4), (2, 2, 4)]
    >>> triplets(6)
    [(1, 1, 2), (1, 2, 3), (1, 3, 4), (1, 4, 5), (2, 2, 4), (2, 3, 5)]
"""
