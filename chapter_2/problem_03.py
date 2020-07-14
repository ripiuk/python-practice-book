"""
Problem:
    What happens when the above `sum` function is called with a list of strings?
    Can you make your `sum` function work for a list of strings as well.

Solution:
    >>> from functools import reduce
    >>> import typing as typ
    >>> def sum_(list_: typ.List[str]) -> str:
    ...     return reduce(lambda x, y: x + y, list_)

    >>> sum_(['hello', 'world'])
    'helloworld'
    >>> sum_(['aa', 'bb', 'cc'])
    'aabbcc'
"""
