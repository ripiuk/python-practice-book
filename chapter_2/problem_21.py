"""
Problem:
    Write a program wrap.py that takes filename and width
    as aruguments and wraps the lines longer than width.

Example:
    $ cat she.txt
    She sells seashells on the seashore;
    The shells that she sells are seashells I'm sure.
    So if she sells seashells on the seashore,
    I'm sure that the shells are seashore shells.

    $ python chapter_2/problem_21.py she.txt 30
    She sells seashells on the sea
    shore;
    The shells that she sells are
    seashells I'm sure.
    So if she sells seashells on t
    he seashore,
    I'm sure that the shells are s
    eashore shells.
"""

import os
import sys


def main():
    """
    Check the function with the data from the example above
    >>> file_content = '''She sells seashells on the seashore;
    ... The shells that she sells are seashells I'm sure.
    ... So if she sells seashells on the seashore,
    ... I'm sure that the shells are seashore shells.'''
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile() as tmp_f:
    ...     _ = tmp_f.write(file_content.encode())
    ...     _ = tmp_f.seek(0)
    ...     sys.argv = [sys.argv[0], tmp_f.name, '30']
    ...     main()
    She sells seashells on the sea
    shore;
    The shells that she sells are
    seashells I'm sure.
    So if she sells seashells on t
    he seashore,
    I'm sure that the shells are s
    eashore shells.

    No arguments provided
    >>> sys.argv = sys.argv[:1]
    >>> main()
    'Please add file name and width as an argument'

    No width argument provided
    >>> sys.argv = [sys.argv[0], 'some_file.txt']
    >>> main()
    'Please add file name and width as an argument'

    File do not exists
    >>> sys.argv = [sys.argv[0], 'not_existing_file.txt', '10']
    >>> main()
    "Can not find the file path: 'not_existing_file.txt'"

    Width is not integer
    >>> with tempfile.NamedTemporaryFile() as tmp_f:
    ...     _ = tmp_f.write(file_content.encode())
    ...     _ = tmp_f.seek(0)
    ...     sys.argv = [sys.argv[0], tmp_f.name, 'str']
    ...     main()
    'The width argument should be integer'
    """
    if len(sys.argv) < 3:
        return 'Please add file name and width as an argument'

    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        return f'Can not find the file path: {file_path!r}'

    width = sys.argv[2]
    if not width.isdigit():
        return 'The width argument should be integer'
    width = int(width)

    with open(file_path, 'r') as rev_f:
        for row in rev_f:
            row = row.rstrip()
            for part in [row[i:i+width] for i in range(0, len(row), width)]:
                # rstrip - because we can not add whitespace to doctests
                print(part.rstrip())


if __name__ == '__main__':
    main()
