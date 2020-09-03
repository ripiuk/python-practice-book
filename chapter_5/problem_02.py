"""
Problem:
    Write a program that takes one or more filenames as arguments
    and prints all the lines which are longer than 40 characters.
"""

import sys
import typing as typ
from pathlib import Path


def read_files(files: typ.Tuple[str, ...]) -> typ.Iterator[str]:
    """Read lines from all the files

    Not existing file:
        >>> next(read_files(files=('not_existing_file.txt', )))
        Traceback (most recent call last):
        ...
        FileNotFoundError: Can not find file: 'not_existing_file.txt'

    Multiple files:
        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     first_file = Path(tmp_dir) / 'file1.txt'
        ...     _ = first_file.write_text('first line\\nsecond line')
        ...     second_file = Path(tmp_dir) / 'file2.txt'
        ...     _ = second_file.write_text('third line\\nfourth line')
        ...     list(read_files(files=tuple(map(str, (first_file, second_file)))))
        ['first line', 'second line', 'third line', 'fourth line']

    :param files: files path.
    :return: lines from all the files.
    :raise FileNotFoundError: if file is not exists
    """
    for file in map(Path, files):
        if not file.exists():
            raise FileNotFoundError(f'Can not find file: {str(file)!r}')
        with open(str(file), 'r') as inp_f:
            for line in inp_f:
                yield line.rstrip('\n')


def filter_line_len(lines: typ.Iterator[str], min_len: int) -> typ.Iterator[str]:
    """Filter lines by their length

    Filter by lines length:
        >>> list(filter_line_len(
        ...     lines=(
        ...         ''.join(map(str, range(1, i + 1)))
        ...         for i in range(1, 10)
        ...     ),
        ...     min_len=7))
        ['12345678', '123456789']

    :param lines: lines from files.
    :param min_len: minimal line length.
    :return: filtered lines.
    """
    return filter(lambda x: len(x) > min_len, lines)


def main(*files: str, min_line_len: int = 40) -> None:
    """Read files and print lines which are longer than min_line_len

    Example:
        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     first_file = Path(tmp_dir) / 'file1.txt'
        ...     _ = first_file.write_text('first line\\nsecond line')
        ...     second_file = Path(tmp_dir) / 'file2.txt'
        ...     _ = second_file.write_text('third line\\nfourth line')
        ...     main(*map(str, (first_file, second_file)), min_line_len=10)
        second line
        fourth line

    :param files: files path.
    :param min_line_len: print lines longer than min_line_len.
    :return: None.
    """
    lines = read_files(files=files)
    for line in filter_line_len(lines=lines, min_len=min_line_len):
        print(line)


if __name__ == "__main__":
    main(*sys.argv[1:])
