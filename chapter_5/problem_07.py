"""
Problem:
    Write a program `split.py`, that takes an integer `n` and a filename
    as command line arguments and splits the file into multiple small files
    with each having `n` lines.
"""

import sys
import typing as typ
from pathlib import Path
from itertools import islice, chain


def chunks(iterable: typ.Iterable[typ.Any], size: int) -> typ.Iterator[typ.Any]:
    """Breaks iterable object into chunks

    Example:
        >>> list(map(list, chunks(iterable=range(1, 11), size=4)))
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]]

    :param iterable: iterable object.
    :param size: chunk size.
    :return: chunked iterator.
    """
    iterator = iter(iterable)
    for first in iterator:
        yield chain([first], islice(iterator, size - 1))


def read_file(file_path: str) -> typ.Iterator[str]:
    """Read lines from the file

    Read file:
        >>> import tempfile
        >>> with tempfile.NamedTemporaryFile() as tmp_f:
        ...     _ = tmp_f.write(b'first line\\nsecond line')
        ...     _ = tmp_f.seek(0)
        ...     list(read_file(file_path=tmp_f.name))
        ['first line\\n', 'second line']

    :param file_path: file path.
    :return: lines from the file.
    :raise FileNotFoundError: if file is not exists
    """
    with open(file_path, 'r') as inp_f:
        for line in inp_f:
            yield line


def main(file_path: str, lines_num: int, out_dir_path: str = '') -> None:
    """Splits the file into multiple small files
    with each having `lines_num` lines.

    Not existing file:
        >>> main(file_path='not_existing_file.py', lines_num=1)
        Traceback (most recent call last):
        ...
        FileNotFoundError: Can not find the file: 'not_existing_file.py'

    Directory instead of file:
        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     main(file_path=tmp_dir, lines_num=1)
        Traceback (most recent call last):
        ...
        ValueError: The /tmp/... is not a file!

    Not existing output directory:
        >>> with tempfile.NamedTemporaryFile() as tmp_f:
        ...     main(file_path=tmp_f.name, lines_num=1, out_dir_path='not_existing_dir')
        Traceback (most recent call last):
        ...
        FileNotFoundError: Can not find the directory: 'not_existing_dir'

    File instead of output directory:
        >>> with tempfile.NamedTemporaryFile() as tmp_f:
        ...     main(file_path=tmp_f.name, lines_num=1, out_dir_path=tmp_f.name)
        Traceback (most recent call last):
        ...
        NotADirectoryError: The /tmp/... is not a directory!

    Split file:
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     tmp_dir = Path(tmp_dir)
        ...     file = tmp_dir / 'test_file.txt'
        ...     _ = file.write_text('1\\n2\\n3\\n4\\n5')
        ...     res_dir = tmp_dir / 'out'
        ...     res_dir.mkdir(parents=True, exist_ok=True)
        ...     main(file_path=str(file), lines_num=2, out_dir_path=str(res_dir))
        ...     files = sorted(res_dir.iterdir())
        ...     print(list(map(str, files)))
        ...     for file in  files:
        ...         print(file.read_text())
        ['/tmp/.../out/file0.txt', '/tmp/.../out/file1.txt', '/tmp/.../out/file2.txt']
        1
        2
        <BLANKLINE>
        3
        4
        <BLANKLINE>
        5

    :param file_path: file path.
    :param lines_num: number of lines.
    :param out_dir_path: output directory.
    :return: None
    """
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f'Can not find the file: {str(file_path)!r}')
    if not file_path.is_file():
        raise ValueError(f'The {str(file_path)} is not a file!')

    out_dir_path = Path(out_dir_path)
    if out_dir_path:
        if not out_dir_path.exists():
            raise FileNotFoundError(f'Can not find the directory: {str(out_dir_path)!r}')
        if not out_dir_path.is_dir():
            raise NotADirectoryError(f'The {str(out_dir_path)} is not a directory!')

    for i, lines in enumerate(chunks(read_file(file_path=str(file_path)), lines_num)):
        with open(f'{str(out_dir_path)}/file{i}{file_path.suffix}', 'w+') as res_f:
            res_f.writelines(list(lines))


if __name__ == "__main__":
    main(file_path=sys.argv[1], lines_num=int(sys.argv[2]))
