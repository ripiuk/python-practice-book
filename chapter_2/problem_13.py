"""
Problem:
    Write a function `lensort` to sort a list of strings based on length.

Solution:
    >>> import typing as typ
    >>> def lensort(list_: typ.List[str]) -> typ.List[str]:
    ...     return sorted(list_, key=len)

    >>> lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
    ['c', 'perl', 'java', 'ruby', 'python', 'haskell']
"""
