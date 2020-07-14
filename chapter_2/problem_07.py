"""
Problem:
    Python has built-in functions `min` and `max` to compute minimum and maximum
    of a given list. Provide an implementation for these functions.
    What happens when you call your min and max functions with a list of strings?

Solution:
    # TODO: Make an implementation with *args, **kwargs + key function
    >>> import typing as typ
    >>> def min_(list_: typ.List[typ.Union[int, str]]) -> typ.Union[int, str]:
    ...     if not list_: raise ValueError('Got an empty sequence')
    ...     if len(list_) == 1: return list_[0]
    ...     min_el = list_[0]
    ...     for el in list_[1:]:
    ...         if el < min_el: min_el = el
    ...     return min_el
    >>> def max_(list_: typ.List[typ.Union[int, str]]) -> typ.Union[int, str]:
    ...     if not list_: raise ValueError('Got an empty sequence')
    ...     if len(list_) == 1: return list_[0]
    ...     max_el = list_[0]
    ...     for el in list_[1:]:
    ...         if el > max_el: max_el = el
    ...     return max_el

    >>> min_([1, 9, 0])
    0
    >>> min_(['a', 'b', 'A'])
    'A'
    >>> max_([1, 9, 0])
    9
    >>> max_(['a', 'b', 'A'])
    'b'
"""
