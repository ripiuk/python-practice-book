"""
Problem:
    Improve the program to print the words in the descending order of the
    number of occurrences:

    def word_frequency(words):
        '''Returns frequency of each word given a list of words.'''
        frequency = {}
        for w in words:
            frequency[w] = frequency.get(w, 0) + 1
        return frequency

    def read_words(filename):
        return open(filename).read().split()

    def main(filename):
        frequency = word_frequency(read_words(filename))
        for word, count in frequency.items():
            print(word, count)

    if __name__ == "__main__":
        import sys
        main(sys.argv[1])
"""

import tempfile
import typing as typ
from pathlib import Path
from collections import defaultdict


def word_frequency(words: typ.Iterable[str]) -> typ.Dict[str, int]:
    """Count frequency of each word

    Example:
        >>> word_frequency(['a', 'b', 'a'])
        {'a': 2, 'b': 1}

    :param words: iterable sequence of words
    :return: sorted frequency of each word from the sequence
    """
    # NOTE: we can use `collections.Counter` here instead
    frequency = defaultdict(int)
    for w in words:
        frequency[w] += 1
    return dict(
        sorted(
            frequency.items(),
            key=lambda item: item[1],
            reverse=True,
        )
    )


def read_words(filename: str) -> typ.List[str]:
    """Get words from a file

    Example:
        >>> file_content = 'first line\\nsecond line'
        >>> with tempfile.NamedTemporaryFile() as tmp_f:
        ...     _ = tmp_f.write(file_content.encode())
        ...     _ = tmp_f.seek(0)
        ...     read_words(tmp_f.name)
        ['first', 'line', 'second', 'line']

    :param filename: path to a local file
    :return: sequence of words from the file
    """
    return Path(filename).read_text().split()


def main(filename: str) -> None:
    """Entry point

    Example:
        >>> file_content = 'first line\\nsecond line'
        >>> with tempfile.NamedTemporaryFile() as tmp_f:
        ...     _ = tmp_f.write(file_content.encode())
        ...     _ = tmp_f.seek(0)
        ...     main(tmp_f.name)
        line 2
        first 1
        second 1

    :param filename: path to a local file
    :return: None
    """
    frequency = word_frequency(read_words(filename))
    for word, count in frequency.items():
        print(word, count)


if __name__ == "__main__":
    import sys
    main(sys.argv[1])
