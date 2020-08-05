"""
Problem:
    Write a program to list all the files in the given directory
    along with their length and last modification time.
    The output should contain one line for each file containing filename,
    length and modification date separated by tabs.

    Hint: see help for `os.stat`.
"""

import sys
import time
from pathlib import Path


def main(dir_path: Path, byte_mode: bool = False) -> None:
    """ list all the files in the given directory along with their stats

    Not existing directory:
        >>> main(dir_path=Path('/not/existing/directory'))
        Can not find the directory path: '/not/existing/directory'

    File path instead of directory path:
        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     for i in range(1, 3):
        ...         file_path = Path(tmp_dir) / f'file{i}.txt'
        ...         _ = file_path.write_text('text')
        ...     main(dir_path=file_path, byte_mode=True)
        b'/tmp/.../file1.txt\\t4\\t...'
        b'/tmp/.../file2.txt\\t4\\t...'

    Directory path:
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     for i in range(1, 3):
        ...         (Path(tmp_dir) / f'file{i}.txt').touch()
        ...     main(dir_path=Path(tmp_dir), byte_mode=True)
        b'/tmp/.../file1.txt\\t0\\t...'
        b'/tmp/.../file2.txt\\t0\\t...'

    :param dir_path: path to the needed directory
    :param byte_mode: output as bytes (for tests)
    :return: None
    """
    if not dir_path.exists():
        print(f'Can not find the directory path: {str(dir_path)!r}')
        return

    if dir_path.is_file():
        dir_path = dir_path.parent

    res = {
        str(item): {
            'size': (file_info := item.stat()).st_size,
            'mtime': time.asctime(time.localtime(file_info.st_mtime))
        }
        for item in dir_path.iterdir()
        if item.is_file()
    }

    max_f_name_len, max_size_len, max_mtime_len = (
        max(map(len, column))
        for column in
        zip(
            *(
                (f_name, str(f_info['size']), f_info['mtime'])
                for f_name, f_info in res.items()
            )
        )
    )

    for f_name, f_info in res.items():
        out = f'{f_name:<{max_f_name_len}}\t' \
              f'{f_info["size"]:<{max_size_len}}\t' \
              f'{f_info["mtime"]:<{max_mtime_len}}'
        print(out.encode() if byte_mode else out)


if __name__ == "__main__":
    path: Path = Path(sys.argv[1]) \
        if len(sys.argv) >= 2 \
        else Path(sys.argv[0])
    main(dir_path=path)
