"""
Problem:
    Implement a function `product` to multiply 2 numbers recursively
    using `+` and `-` operators only.

Solution:
    >>> def product(a: int, b: int) -> int:
    ...     a, b = (b, a) if b > a else (b, a)  # To protect against very deep recursion
    ...     return a + product(a, b-1) if b != 0 else b

    >>> product(2, 2)
    4
    >>> product(4, 2)
    8
    >>> product(3, 10)
    30
    >>> product(1, 238)
    238
    >>> product(41, 123)
    5043
    >>> product(123456789, 1)
    123456789
    >>> product(32, 123456789)
    3950617248
"""
