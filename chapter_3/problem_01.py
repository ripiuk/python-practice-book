"""
Problem:
    Write a program to list all files in the given directory.
"""

import sys
from pathlib import Path
from functools import partial


def main(dir_path: Path, sort: bool = False) -> None:
    """List all files in the given directory

    Not existing directory:
        >>> main(dir_path=Path('/not/existing/directory'))
        Can not find the directory path: '/not/existing/directory'

    File path instead of directory path:
        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     file_path = Path(tmp_dir) / 'file1.txt'
        ...     file_path.touch()
        ...     (Path(tmp_dir) / 'file2.txt').touch()
        ...     main(dir_path=file_path)
        /tmp/.../file1.txt
        /tmp/.../file2.txt

    Directory path:
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     for i in range(1, 4):
        ...         (Path(tmp_dir) / f'file{i}.txt').touch()
        ...     main(dir_path=Path(tmp_dir), sort=True)
        /tmp/.../file1.txt
        /tmp/.../file2.txt
        /tmp/.../file3.txt

    :param dir_path: path to the needed directory
    :param sort: sort files by name
    :return: None
    """
    if not dir_path.exists():
        print(f'Can not find the directory path: {str(dir_path)!r}')
        return

    if dir_path.is_file():
        dir_path = dir_path.parent

    iter_dir = partial(sorted, dir_path.iterdir()) if sort else dir_path.iterdir
    for item in iter_dir():
        print(item) if item.is_file() else None


if __name__ == "__main__":
    path: Path = Path(sys.argv[1]) \
        if len(sys.argv) >= 2 \
        else Path(sys.argv[0])
    main(dir_path=path)
