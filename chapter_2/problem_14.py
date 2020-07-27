"""
Problem:
    Improve the `unique` function written in previous problems
    to take an optional key function as argument and use the
    return value of the key function to check for uniqueness.

Solution:
    >>> import typing as typ
    >>> def unique(list_: typ.List[str], key: typ.Callable[[str], str] = None) -> typ.List[str]:
    ...     # NOTE: I tried not to use list(set(list_)) here
    ...     list_, checked = [key(el) for el in list_] if key else list_, set()
    ...     return [el for el in list_ if el not in checked and (checked.add(el) or True)]

    >>> unique(["python", "java", "Python", "Java"], key=lambda s: s.lower())
    ['python', 'java']
"""
