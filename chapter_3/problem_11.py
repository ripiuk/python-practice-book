"""
Problem:
    Write a python program `zip.py` to create a zip file.
    The program should take name of zip file as first argument and files
    to add as rest of the arguments.

Example:
    $ python zip.py foo.zip file1.txt file2.txt
"""


import sys
import zipfile
from pathlib import Path


def main(file_name: str, *files) -> None:
    """Create a zip file

    File already exists:
        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     (Path(tmp_dir) / f'test_file.zip').touch()
        ...     main(str(Path(tmp_dir) / f'test_file.zip'))
        File /tmp/.../test_file.zip already exists

    File already exists without .zip suffix:
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     (Path(tmp_dir) / f'test_file.zip').touch()
        ...     main(str(Path(tmp_dir) / f'test_file'))
        File /tmp/.../test_file.zip already exists

    Add directory to the zip file:
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     (Path(tmp_dir) / 'directory').mkdir(parents=True, exist_ok=True)
        ...     main(str(Path(tmp_dir) / f'test_file'), str(Path(tmp_dir) / 'directory'))
        Can not add file '/tmp/.../directory' to the zip file. Skipping.
        ZIP file '/tmp/.../test_file.zip' created successfully.

    Add not existing file to the zip file:
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     main(str(Path(tmp_dir) / f'test_file'), str(Path(tmp_dir) / 'not_existing_file.txt'))
        ...     with zipfile.ZipFile(str(Path(tmp_dir) / f'test_file.zip')) as zip_f:
        ...         for name in zip_f.namelist():
        ...             print(name)
        Can not add file '/tmp/.../not_existing_file.txt' to the zip file. Skipping.
        ZIP file '/tmp/.../test_file.zip' created successfully.

    Add existing file to the zip file:
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     file = (Path(tmp_dir) / 'existing_file.txt')
        ...     file.touch()
        ...     main(str(Path(tmp_dir) / f'test_file.zip'), str(file))
        ...     with zipfile.ZipFile(str(Path(tmp_dir) / f'test_file.zip')) as zip_f:
        ...         for name in zip_f.namelist():
        ...             print(name)
        ZIP file '/tmp/.../test_file.zip' created successfully.
        tmp/.../existing_file.txt

    Add many files to the zip file:
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     files = [Path(tmp_dir) / f'file{i}' for i in range(1, 6)]
        ...     for file in files:
        ...         file.touch()
        ...     main(str(Path(tmp_dir) / f'test_file.zip'), *map(str, files))
        ...     with zipfile.ZipFile(str(Path(tmp_dir) / f'test_file.zip')) as zip_f:
        ...         for name in zip_f.namelist():
        ...             print(name)
        ZIP file '/tmp/.../test_file.zip' created successfully.
        tmp/.../file1
        tmp/.../file2
        tmp/.../file3
        tmp/.../file4
        tmp/.../file5

    :param file_name: Zip file name.
    :return: None.
    """
    file_name = file_name if file_name.endswith('.zip') else f'{file_name}.zip'
    if Path(file_name).exists():
        print(f'File {file_name} already exists')
        return

    with zipfile.ZipFile(file_name, "w", zipfile.ZIP_DEFLATED) as zip_f:
        for file in map(Path, files):
            if not file.exists() or not file.is_file():
                print(f'Can not add file {str(file)!r} to the zip file. Skipping.')
                continue
            zip_f.write(str(file))
    print(f'ZIP file {file_name!r} created successfully.')


if __name__ == "__main__":
    main(file_name=sys.argv[1], *sys.argv[2:])
