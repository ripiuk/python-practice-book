"""
Problem:
    Write a function `valuesort` to sort values of a dictionary based on the key.

Solution:
    >>> import typing as typ
    >>> def valuesort(dict_: dict) -> typ.List[typ.Any]:
    ...     return [v for k, v in sorted(dict_.items(), key=lambda x: x[0])]

    >>> valuesort({'x': 1, 'y': 2, 'a': 3})
    [3, 1, 2]
    >>> valuesort({'some': 123, 'keys': 0, 'here': 8})
    [8, 0, 123]
"""
