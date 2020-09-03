"""
Problem:
    Write a function `findfiles` that recursively descends the directory tree
    for the specified directory and generates paths of all the files in the tree.
"""

import sys
import typing as typ
from pathlib import Path
from functools import partial


def find_files(dir_path: Path, absolute_path: bool = True) -> typ.Iterator[str]:
    """Generates paths of all the files in the directory tree recursively

    Not existing directory:
        >>> list(find_files(dir_path=Path('not_existing_path')))
        Traceback (most recent call last):
        ...
        FileNotFoundError: [Errno 2] No such file or directory: 'not_existing_path'

    Empty directory:
        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     tmp_dir = Path(tmp_dir)
        ...     list(find_files(dir_path=tmp_dir))
        []

    Nested structure:
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     tmp_dir = Path(tmp_dir)
        ...     for i in range(1, 3):
        ...         (tmp_dir / f'file{i}.txt').touch()
        ...     (tmp_dir / 'subdir').mkdir(parents=True, exist_ok=True)
        ...     for i in range(1, 4):
        ...         (tmp_dir / 'subdir' / f'file{i}.py').touch()
        ...     for file_path in sorted(list(find_files(dir_path=tmp_dir))):
        ...         print(file_path)
        /tmp/.../file1.txt
        /tmp/.../file2.txt
        /tmp/.../subdir/file1.py
        /tmp/.../subdir/file2.py
        /tmp/.../subdir/file3.py

    :param dir_path: root directory path.
    :param absolute_path: use absolute version of path.
    :return: files path.
    """
    for item in dir_path.iterdir():
        if item.is_dir():
            yield from find_files(dir_path=item)
        else:
            yield str(item.absolute() if absolute_path else item)


def main(dir_path: str, sort: bool = False) -> None:
    """Recursively descends the directory and print files path

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

    Nested structure:
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     tmp_dir = Path(tmp_dir)
        ...     for i in range(1, 3):
        ...         (tmp_dir / f'file{i}.txt').touch()
        ...     (tmp_dir / 'subdir').mkdir(parents=True, exist_ok=True)
        ...     for i in range(1, 3):
        ...         (tmp_dir / 'subdir' / f'file{i}.py').touch()
        ...     main(dir_path=str(tmp_dir), sort=True)
        /tmp/.../file1.txt
        /tmp/.../file2.txt
        /tmp/.../subdir/file1.py
        /tmp/.../subdir/file2.py

    :param dir_path: root directory path.
    :param sort: sort files by name.
    :return: None
    """
    dir_path = Path(dir_path)
    if not dir_path.exists():
        raise FileNotFoundError(f'Can not find the directory: {str(dir_path)!r}')
    if not dir_path.is_dir():
        raise NotADirectoryError(f'The {str(dir_path)} is not a directory!')

    get_files = partial(find_files, dir_path=dir_path, absolute_path=True)
    for file_path in sorted(get_files()) if sort else get_files():
        print(file_path)


if __name__ == "__main__":
    main(dir_path=sys.argv[1])
