"""
Problem:
    Reimplement the `unique` function implemented in the earlier examples using sets.

Solution:
    >>> import typing as typ
    >>> def unique(list_: typ.List[str], key: typ.Callable[[str], str] = None) -> typ.List[str]:
    ...     return sorted(set([key(el) for el in list_] if key else list_))

    >>> unique(["python", "java", "Python", "Java"], key=lambda s: s.lower())
    ['java', 'python']
"""
