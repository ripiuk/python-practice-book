"""
Problem:
    What will be the output of the following program?

    >>> x = 1
    >>> def f():
    ...     y = x
    ...     x = 2
    ...     return x + y

    print(x)
    print(f())
    print(x)

Solution:
    >>> print(x)
    1
    >>> print(f())
    Traceback (most recent call last):
    ...
    UnboundLocalError: local variable 'x' referenced before assignment
    >>> print(x)
    1
"""
