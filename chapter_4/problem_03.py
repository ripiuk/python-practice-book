"""
Problem:
    What will be the output of the following program?

Solution:
    >>> try:
    ...     print("a")
    ...     raise Exception("doom")
    ... except:
    ...     print("b")
    ... else:
    ...     print("c")
    ... finally:
    ...     print("d")
    a
    b
    d
"""
