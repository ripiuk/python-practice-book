"""
Problem:
    What will the output of the following program.

Solution:
    >>> class A:
    ...     def f(self):
    ...         return self.g()
    ...
    ...     def g(self):
    ...         return 'A'

    >>> class B(A):
    ...     def g(self):
    ...         return 'B'

    >>> a = A()
    >>> b = B()
    >>> print(a.f(), b.f())
    A B
    >>> print(a.g(), b.g())
    A B
"""
