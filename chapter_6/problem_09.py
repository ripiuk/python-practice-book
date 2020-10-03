"""
Problem:
    Write a function `permute` to compute all possible permutations
    of elements of a given list.
"""

import itertools
import typing as typ


def permute(list_: typ.List[typ.Any]) -> typ.List[typ.List[typ.Any]]:
    """Compute all possible permutations of elements of a given list.

    Tests:
        >>> permute([1, 2, 3])
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

        >>> permute([1, 2, 3, 4])  # doctest: +NORMALIZE_WHITESPACE
        [[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3],
         [1, 4, 3, 2], [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1],
         [2, 4, 1, 3], [2, 4, 3, 1], [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4],
         [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2],
         [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]]

    :param list_: list of elements
    :return: possible permutations
    """
    return [list_] \
        if len(list_) == 1 \
        else [
            [el] + p
            for i, el in enumerate(list_)
            for p in permute(list_[:i] + list_[i+1:])
        ]


def permute_itertools(iterable: typ.Iterable) -> typ.List[typ.Tuple[typ.Any]]:
    """Compute all possible permutations of elements
    of a given list using `itertools.permutations`

    Tests:
        >>> permute_itertools([1, 2, 3])
        [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

        >>> permute_itertools([1, 2, 3, 4])  # doctest: +NORMALIZE_WHITESPACE
        [(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3),
         (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1),
         (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4),
         (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2),
         (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)]

        >>> permute_itertools('123')  # doctest: +NORMALIZE_WHITESPACE
        [('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'),
         ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]

    :param iterable: elements for permutations
    :return: possible permutations
    """
    return list(itertools.permutations(iterable))
