"""
Problem:
    Write a program to find anagrams in a given list of words.
    Two words are called anagrams if one word can be formed by rearranging
    letters of another. For example `eat`, `ate` and `tea` are anagrams.

Solution:
    >>> import typing as typ
    >>> def anagrams(iterable: typ.Iterable[str]) -> typ.List[typ.List[str]]:
    ...     checked_words = set()
    ...     return [
    ...         [
    ...             check_word
    ...             for check_word in iterable
    ...             if sorted(list(word)) == sorted(list(check_word))
    ...             and (checked_words.add(check_word) or True)
    ...         ] for word in iterable
    ...         if word not in checked_words
    ...     ]

    >>> anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node'])
    [['eat', 'ate', 'tea'], ['done', 'node'], ['soup']]
"""
