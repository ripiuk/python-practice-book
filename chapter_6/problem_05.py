"""
Problem:
    Write a function `tree_reverse` to reverse elements of a nested-list recursively.

Solution:
    >>> import typing as typ
    >>> from collections.abc import Iterable

    >>> def _is_reversible(el: typ.Any) -> bool:
    ...     return (
    ...         hasattr(el, '__len__') and callable(el.__len__)
    ...         and hasattr(el, '__getitem__') and callable(el.__getitem__)
    ...     ) or (
    ...         hasattr(el, '__reverse__') and callable(el.__reverse__)
    ...     ) or (
    ...         hasattr(el, '__reversed__') and callable(el.__reversed__)
    ...     )

    >>> def tree_reverse(iterables: typ.Iterable[typ.Any]) -> typ.List[typ.Any]:
    ...     return list(reversed(
    ...         [tree_reverse(el) for el in iterables]
    ...         if isinstance(iterables, Iterable)
    ...         and not isinstance(iterables, (str, bytes))  # we can skip bytes check here
    ...         else iterables
    ...     )) if _is_reversible(iterables) \\
    ...        and not isinstance(iterables, bytes) \\
    ...        else iterables

    >>> def tree_reverse_transform_first(iterables: typ.Iterable[typ.Any]) -> typ.List[typ.Any]:
    ...     if isinstance(iterables, Iterable) and not isinstance(iterables, (str, bytes)):
    ...         iterables = [tree_reverse_transform_first(el) for el in iterables]
    ...     return list(reversed(iterables)) \\
    ...         if _is_reversible(iterables) and not isinstance(iterables, bytes) \\
    ...         else iterables


    >>> tree_reverse([[1, 2], [3, [4, 5]], 6])
    [6, [[5, 4], 3], [2, 1]]

    >>> tree_reverse((1, (2, 3, (4, ), 5), 6, (7, ),8))
    [8, [7], 6, [5, [4], 3, 2], 1]

    >>> tree_reverse('test text')
    ['t', 'x', 'e', 't', ' ', 't', 's', 'e', 't']

    >>> tree_reverse(range(1, 9))
    [8, 7, 6, 5, 4, 3, 2, 1]

    >>> tree_reverse([1, [2.0, '3'], ({4}, {5: 5, '6': 'skipped_value'}, range(7, 10), (b'10', ))])
    [[[b'10'], [9, 8, 7], [['6'], 5], {4}], [['3'], 2.0], 1]
"""
