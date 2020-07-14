"""
Problem:
    What will be the output of the following program?

    >>> x = 1
    >>> def f():
    ...     x = 2
    ...     return x

    print(x)
    print(f())
    print(x)

Solution:
    >>> print(x)
    1
    >>> print(f())
    2
    >>> print(x)
    1
"""
