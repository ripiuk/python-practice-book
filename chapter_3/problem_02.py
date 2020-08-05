"""
Problem:
    Write a program `extcount.py` to count number of files for each extension
    in the given directory. The program should take a directory name
    as argument and print count and extension for each available file extension.

        $ python extcount.py src/
        14 py
        4 txt
        1 csv
"""

import sys
from pathlib import Path
from collections import Counter


def main(dir_path: Path) -> None:
    """Count number of files for each extension in the given directory

    Not existing directory:
        >>> main(dir_path=Path('/not/existing/directory'))
        Can not find the directory path: '/not/existing/directory'

    File path instead of directory path:
        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     for i in range(12):
        ...         file_path = Path(tmp_dir) / f'file{i}.txt'
        ...         file_path.touch()
        ...     main(dir_path=file_path)
        12 .txt

    Directory path:
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     for i in range(14):
        ...         (Path(tmp_dir) / f'file{i}.py').touch()
        ...     for i in range(4):
        ...         (Path(tmp_dir) / f'file{i}.txt').touch()
        ...     (Path(tmp_dir) / 'file.csv').touch()
        ...     main(dir_path=Path(tmp_dir))
        14 .py
        4 .txt
        1 .csv

    :param dir_path: path to the needed directory
    :return: None
    """
    if not dir_path.exists():
        print(f'Can not find the directory path: {str(dir_path)!r}')
        return

    if dir_path.is_file():
        dir_path = dir_path.parent

    for extension, count in Counter((
            item.suffix
            for item in dir_path.iterdir()
            if item.is_file()
    )).items():
        print(count, extension)


if __name__ == "__main__":
    path: Path = Path(sys.argv[1]) \
        if len(sys.argv) >= 2 \
        else Path(sys.argv[0])
    main(dir_path=path)
