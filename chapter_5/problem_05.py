"""
Problem:
    Write a function to compute the total number of lines of code in all
    python files in the specified directory recursively.
"""

import sys
import typing as typ
from pathlib import Path


def read_files(files: typ.Iterator[str]) -> typ.Iterator[str]:
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


def find_files(dir_path: Path, extension: str) -> typ.Iterator[str]:
    """Search for files with the needed extension in the directory tree recursively

    Not existing directory:
        >>> list(find_files(dir_path=Path('not_existing_path'), extension='txt'))
        Traceback (most recent call last):
        ...
        FileNotFoundError: [Errno 2] No such file or directory: 'not_existing_path'

    Empty directory:
        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     tmp_dir = Path(tmp_dir)
        ...     list(find_files(dir_path=tmp_dir, extension='txt'))
        []

    Nested structure:
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     tmp_dir = Path(tmp_dir)
        ...     for i in range(1, 3):
        ...         (tmp_dir / f'file{i}.txt').touch()
        ...     (tmp_dir / 'subdir').mkdir(parents=True, exist_ok=True)
        ...     for i in range(1, 4):
        ...         (tmp_dir / 'subdir' / f'file{i}.py').touch()
        ...     for file_path in sorted(list(find_files(dir_path=tmp_dir, extension='py'))):
        ...         print(file_path)
        /tmp/.../subdir/file1.py
        /tmp/.../subdir/file2.py
        /tmp/.../subdir/file3.py

    :param dir_path: root directory path.
    :param extension: file extension.
    :return: files path.
    """
    for item in dir_path.iterdir():
        if item.is_dir():
            yield from find_files(dir_path=item, extension=extension)
        elif item.suffix.lstrip('.') == extension.lstrip('.'):
            yield str(item)


def main(dir_path: str, extension: str = 'py') -> None:
    """Count all files with needed extension in directory recursively

    Not existing directory:
        >>> main(dir_path='not_existing_dir')
        Traceback (most recent call last):
        ...
        FileNotFoundError: Can not find the directory: 'not_existing_dir'

    File instead of directory:
        >>> import tempfile
        >>> with tempfile.NamedTemporaryFile() as tmp_f:
        ...     main(dir_path=tmp_f.name)
        Traceback (most recent call last):
        ...
        NotADirectoryError: The /tmp/... is not a directory!

    Empty directory:
        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     main(dir_path=tmp_dir)
        0

    One file:
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     tmp_dir = Path(tmp_dir)
        ...     file = tmp_dir / f'test_file.py'
        ...     _ = file.write_text('1\\n2\\n3')
        ...     main(dir_path=str(tmp_dir), extension='py')
        3

    Empty files in subdir:
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     tmp_dir = Path(tmp_dir)
        ...     (tmp_dir / 'subdir').mkdir(parents=True, exist_ok=True)
        ...     for i in range(1, 3):
        ...         (tmp_dir / 'subdir' / f'file{i}.py').touch()
        ...     main(dir_path=str(tmp_dir), extension='py')
        0

    Nested structure:
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     tmp_dir = Path(tmp_dir)
        ...     for i in range(1, 4):
        ...         (tmp_dir / f'file{i}.txt').touch()
        ...     (tmp_dir / 'subdir').mkdir(parents=True, exist_ok=True)
        ...     for i in range(1, 3):
        ...         file = tmp_dir / 'subdir' / f'file{i}.py'
        ...         _ = file.write_text('first row\\nsecond row')
        ...     main(dir_path=str(tmp_dir), extension='py')
        4

    :param dir_path: root directory path.
    :param extension: file extension.
    :return: None
    """
    dir_path = Path(dir_path)
    if not dir_path.exists():
        raise FileNotFoundError(f'Can not find the directory: {str(dir_path)!r}')
    if not dir_path.is_dir():
        raise NotADirectoryError(f'The {str(dir_path)} is not a directory!')

    files = find_files(dir_path=dir_path, extension=extension)
    print(sum(map(bool, read_files(files=files))))


if __name__ == "__main__":
    main(dir_path=sys.argv[1])
