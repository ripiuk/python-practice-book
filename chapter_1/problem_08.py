"""
Problem:
    Write a function istrcmp to compare two strings, ignoring the case.

Solution:
    >>> def istrcmp(*args: str) -> bool:
    ...     return len(set(word.lower() for word in args)) == 1

    >>> istrcmp('python', 'Python')
    True
    >>> istrcmp('LaTeX', 'Latex')
    True
    >>> istrcmp('a', 'b')
    False
"""
