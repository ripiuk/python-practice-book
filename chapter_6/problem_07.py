"""
Problem:
    Implement a program `dirtree.py` that takes a directory as argument
    and prints all the files in that directory recursively as a tree.
    (Note: duplicates chapter_3/problem_04.py problem and solution)

Example:
    $ python dirtree.py foo/
    foo/
    |-- a.txt
    |-- b.txt
    |-- bar/
    |   |-- p.txt
    |   `-- q.txt
    `-- c.txt
"""

import sys
import typing as typ
from pathlib import Path


def main(dir_path: Path, sort=False) -> None:
    """Print all the files in a directory recursively as a tree

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
        ...     main(dir_path=file_path, sort=True)
        ... finally:
        ...     shutil.rmtree(dir_path)  # we can not use dir_path.rmdir() here
        [test_problem_03_file_path]
        ├── file2.py
        ├── [subdir]
        │   ├── file1.txt
        │   ├── file2.txt
        │   └── [another_dir]
        │       └── file1.txt
        └── file1.py

    Directory path:
        >>> dir_path = Path('/tmp/test_problem_03_dir_path')
        >>> try:
        ...     dir_path.mkdir(parents=True, exist_ok=True)
        ...     for i in range(1, 3):
        ...         (dir_path / f'file{i}.txt').touch()
        ...     (dir_path / 'subdir').mkdir(parents=True, exist_ok=True)
        ...     for i in range(1, 4):
        ...         (dir_path / 'subdir' / f'file{i}.py').touch()
        ...     main(dir_path=dir_path, sort=True)
        ... finally:
        ...     shutil.rmtree(dir_path)  # we can not use dir_path.rmdir() here
        [test_problem_03_dir_path]
        ├── file2.txt
        ├── [subdir]
        │   ├── file2.py
        │   ├── file3.py
        │   └── file1.py
        └── file1.txt

    Empty directory:
        >>> dir_path = Path('/tmp/test_problem_03_empty_dir')
        >>> try:
        ...     dir_path.mkdir(parents=True, exist_ok=True)
        ...     main(dir_path=dir_path)
        ... finally:
        ...     shutil.rmtree(dir_path)  # we can not use dir_path.rmdir() here
        [test_problem_03_empty_dir]

        >>> dir_path = Path('/tmp/test_problem_03_empty_dir')
        >>> try:
        ...     dir_path.mkdir(parents=True, exist_ok=True)
        ...     (dir_path / 'subdir' / 'another_dir').mkdir(parents=True, exist_ok=True)
        ...     main(dir_path=dir_path)
        ... finally:
        ...     shutil.rmtree(dir_path)  # we can not use dir_path.rmdir() here
        [test_problem_03_empty_dir]
        └── [subdir]
            └── [another_dir]

    Only one file inside the directory:
        >>> dir_path = Path('/tmp/test_problem_03_one_file')
        >>> try:
        ...     dir_path.mkdir(parents=True, exist_ok=True)
        ...     (dir_path / f'one_file.py').touch()
        ...     main(dir_path=dir_path)
        ... finally:
        ...     shutil.rmtree(dir_path)  # we can not use dir_path.rmdir() here
        [test_problem_03_one_file]
        └── one_file.py

    :param dir_path: path to the needed directory
    :param sort: sort files and dirs by name
    :return: None
    """
    if not dir_path.exists():
        print(f'Can not find the directory path: {str(dir_path)!r}')
        return

    if dir_path.is_file():
        dir_path = dir_path.parent

    print(f'[{dir_path.name}]')
    print_tree(dir_path=dir_path, sort=sort)


def print_tree(
        dir_path: Path,
        lvl: int = 0,
        stack_on_level: typ.Dict[int, bool] = None,
        sort: bool = False,
) -> None:
    """Print the needed folder tree recursively

    :param dir_path: path to the needed directory.
    :param lvl: current recursion level.
    :param stack_on_level: shows if we need stack char on recursion levels.
    :param sort: sort items by name.
    :return: None
    """
    if stack_on_level is None:
        stack_on_level = dict()

    dir_content = iter(sorted(dir_path.iterdir())) if sort else dir_path.iterdir()
    first_item = next(dir_content, None)
    stack_on_level[lvl] = True

    for item in dir_content:
        _print_element(
            item=item,
            lvl=lvl,
            stack_on_level=stack_on_level,
            sort=sort,
        )

    if first_item:
        stack_on_level[lvl] = False
        _print_element(
            item=first_item,
            lvl=lvl,
            stack_on_level=stack_on_level,
            sort=sort,
            prefix_char='└──',
        )


def _print_element(
        item: Path,
        lvl: int,
        stack_on_level: typ.Dict[int, bool],
        sort: bool,
        prefix_char: str = '├──',
) -> None:
    """Print current element from the directory tree

    The last file, first level:
        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     file = Path(tmp_dir) / 'file1.txt'
        ...     file.touch()
        ...     _print_element(item=file, lvl=0, stack_on_level={0: True}, sort=False, prefix_char='└──')
        └── file1.txt

    File in the middle, third level, stack missed on the second level:
        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     file = Path(tmp_dir) / 'file1.txt'
        ...     file.touch()
        ...     _print_element(item=file, lvl=2, stack_on_level={0: True, 1: False, 2: True},
        ...                    sort=False, prefix_char='├──')
        │       ├── file1.txt

    :param item: path to the needed item in a directory.
    :param lvl: current recursion level.
    :param stack_on_level: shows if we need stack char on recursion levels.
    :param sort: sort items by name.
    :param prefix_char: prefix char for the current item.
    :return: None
    """
    item_name = f'[{item.name}]' if item.is_dir() else item.name
    print(
        f'{"".join("│   " if stack_on_level[i] else "    " for i in range(lvl))}'
        f'{prefix_char} {item_name}'
    )
    if item.is_dir():
        print_tree(dir_path=item, lvl=lvl + 1, stack_on_level=stack_on_level, sort=sort)


if __name__ == "__main__":
    path: Path = Path(sys.argv[1]) \
        if len(sys.argv) >= 2 \
        else Path(sys.argv[0])
    main(dir_path=path)
