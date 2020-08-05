"""
Problem:
    Write a program to print directory tree. The program should take path of a directory
    as argument and print all the files in it recursively as a tree.

Example:
    $ python dirtree.py foo
    foo
    |-- a.txt
    |-- b.txt
    |-- code
    |   |-- a.py
    |   |-- b.py
    |   |-- docs
    |   |   |-- a.txt
    |   |   \-- b.txt
    |   \-- x.py
    \-- z.txt
"""

import sys
from pathlib import Path


def main(dir_path: Path) -> None:
    """ list all the files in the given directory along with their stats

    Not existing directory:
        >>> main(dir_path=Path('/not/existing/directory'))
        Can not find the directory path: '/not/existing/directory'

    File path instead of directory path:
        NOTE: we can not use tempfile.TemporaryDirectory here
        because we need the directory name
        >>> import shutil
        >>> dir_path = Path('/tmp/test_problem_03_file_path')
        >>> try:
        ...     dir_path.mkdir(parents=True, exist_ok=True)
        ...     for i in range(1, 3):
        ...         file_path = dir_path / f'file{i}.py'
        ...         file_path.touch()
        ...     (dir_path / 'subdir' / 'another_dir').mkdir(parents=True, exist_ok=True)
        ...     (dir_path / 'subdir' / 'file1.txt').touch()
        ...     (dir_path / 'subdir' / 'file2.txt').touch()
        ...     (dir_path / 'subdir' / 'another_dir' / 'file1.txt').touch()
        ...     main(dir_path=file_path)
        ... finally:
        ...     shutil.rmtree(dir_path)  # we can not use dir_path.rmdir() here
        test_problem_03_file_path
        ├── file1.py
        ├── subdir
        │   ├── another_dir
        │   │   └── file1.txt
        │   ├── file2.txt
        │   └── file1.txt
        └── file2.py

    Directory path:
        >>> dir_path = Path('/tmp/test_problem_03_dir_path')
        >>> try:
        ...     dir_path.mkdir(parents=True, exist_ok=True)
        ...     for i in range(1, 3):
        ...         (dir_path / f'file{i}.txt').touch()
        ...     (dir_path / 'subdir').mkdir(parents=True, exist_ok=True)
        ...     for i in range(1, 4):
        ...         (dir_path / 'subdir' / f'file{i}.py').touch()
        ...     main(dir_path=dir_path)
        ... finally:
        ...     shutil.rmtree(dir_path)  # we can not use dir_path.rmdir() here
        test_problem_03_dir_path
        ├── subdir
        │   ├── file1.py
        │   ├── file3.py
        │   └── file2.py
        ├── file2.txt
        └── file1.txt

    Empty directory:
        >>> dir_path = Path('/tmp/test_problem_03_empty_dir')
        >>> try:
        ...     dir_path.mkdir(parents=True, exist_ok=True)
        ...     main(dir_path=dir_path)
        ... finally:
        ...     shutil.rmtree(dir_path)  # we can not use dir_path.rmdir() here
        test_problem_03_empty_dir

    Only one file inside the directory:
        >>> dir_path = Path('/tmp/test_problem_03_one_file')
        >>> try:
        ...     dir_path.mkdir(parents=True, exist_ok=True)
        ...     (dir_path / f'one_file.py').touch()
        ...     main(dir_path=dir_path)
        ... finally:
        ...     shutil.rmtree(dir_path)  # we can not use dir_path.rmdir() here
        test_problem_03_one_file
        └── one_file.py

    :param dir_path: path to the needed directory
    :return: None
    """
    if not dir_path.exists():
        print(f'Can not find the directory path: {str(dir_path)!r}')
        return

    if dir_path.is_file():
        dir_path = dir_path.parent

    print(dir_path.name)
    print_tree(dir_path=dir_path)


def print_tree(dir_path: Path, lvl: int = 0):
    dir_content = dir_path.iterdir()
    first_item = next(dir_content, None)
    for item in dir_content:
        print(f'{"│   " * lvl}├── {item.name}')
        if item.is_dir():
            print_tree(dir_path=item, lvl=lvl + 1)
    if first_item:
        print(f'{"│   " * lvl}└── {first_item.name}')


if __name__ == "__main__":
    path: Path = Path(sys.argv[1]) \
        if len(sys.argv) >= 2 \
        else Path(sys.argv[0])
    main(dir_path=path)
