"""
Problem:
    Write a function `flatten_dict` to flatten a nested dictionary
    by joining the keys with `.` character.

Solution:
    >>> import typing as typ
    >>> def flatten_dict(raw_dict: dict, sep: str = '.') -> dict:
    ...     def flatten(element: dict, parent: str = '') -> typ.Iterator[typ.Tuple[typ.Any, typ.Any]]:
    ...         if isinstance(element, dict):
    ...             for k, v in element.items():
    ...                 yield from flatten(v, f'{parent}{sep}{k}' if parent else k)
    ...         else:
    ...             yield parent, element
    ...     return dict(flatten(raw_dict))

    >>> flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
    {'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}

    >>> flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}, sep='_')
    {'a': 1, 'b_x': 2, 'b_y': 3, 'c': 4}

    >>> flatten_dict({'a': 1, 2: 'b', 3: {'c': 4, 'd': {'e': 5, 'g': [{'d': 6}, 4]}}})
    {'a': 1, 2: 'b', '3.c': 4, '3.d.e': 5, '3.d.g': [{'d': 6}, 4]}
"""
