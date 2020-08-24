"""
Problem:
    What will be the output of the following program?

Solution:
    >>> def f():
    ...     try:
    ...         print("a")
    ...         return
    ...     except:
    ...         print("b")
    ...     else:
    ...         print("c")
    ...     finally:
    ...         print("d")
    >>> f()
    a
    d
"""
