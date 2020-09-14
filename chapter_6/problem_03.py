"""
Problem:
    Write a function `unflatten_dict` to do reverse of `flatten_dict`.

Solution:
    >>> import typing as typ
    >>> def unflatten_dict(raw_dict: dict, sep: str = '.', curr_dict: dict = None) -> dict:
    ...     curr_dict = {} if curr_dict is None else curr_dict
    ...     for k, v in raw_dict.items():
    ...         if isinstance(k, str) and sep in k:
    ...             curr_key, remainder = k.split(sep=sep, maxsplit=1)
    ...             unflatten_dict(raw_dict={remainder: v}, curr_dict=curr_dict.setdefault(curr_key, {}))
    ...         else:
    ...             curr_dict[k] = v
    ...     return curr_dict

    >>> unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
    {'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}

    >>> unflatten_dict({'a': 1, 'b_x': 2, 'b_y': 3, 'c': 4}, sep='_')
    {'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}

    >>> unflatten_dict({'a': 1, 2: 'b', '3.c': 4, '3.d.e': 5, '3.d.f': [{'g': 6}, 4]})
    {'a': 1, 2: 'b', '3': {'c': 4, 'd': {'e': 5, 'f': [{'g': 6}, 4]}}}
"""
