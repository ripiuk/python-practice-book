"""
Problem:
    Write a function `extsort` to sort a list of files based on extension.

Solution:
    >>> import typing as typ
    >>> def extsort(list_: typ.List[str]) -> typ.List[str]:
    ...     return sorted(list_, key=lambda x: x.split('.')[1])

    >>> extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
    ['a.c', 'x.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt']
"""
