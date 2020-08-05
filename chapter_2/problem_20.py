"""
Problem:
    Implement unix command `grep`. The `grep` command takes a string and a file
    as arguments and prints all lines in the file which contain the specified string.

Example:
    $ cat she.txt
    She sells seashells on the seashore;
    The shells that she sells are seashells I'm sure.
    So if she sells seashells on the seashore,
    I'm sure that the shells are seashore shells.

    $ python chapter_2/problem_20.py she.txt sure
    The shells that she sells are seashells I'm sure.
    I'm sure that the shells are seashore shells.
"""

import os
import sys


def main():
    """
    Check the function with the data from the example above:
        >>> file_content = '''She sells seashells on the seashore;
        ... The shells that she sells are seashells I'm sure.
        ... So if she sells seashells on the seashore,
        ... I'm sure that the shells are seashore shells.'''
        >>> import tempfile
        >>> with tempfile.NamedTemporaryFile() as tmp_f:
        ...     _ = tmp_f.write(file_content.encode())
        ...     _ = tmp_f.seek(0)
        ...     sys.argv = [sys.argv[0], tmp_f.name, 'sure']
        ...     main()
        The shells that she sells are seashells I'm sure.
        I'm sure that the shells are seashore shells.

    No arguments provided:
        >>> sys.argv = sys.argv[:1]
        >>> main()
        'Please add file name and a word as an argument'

    No word argument provided:
        >>> sys.argv = [sys.argv[0], 'some_file.txt']
        >>> main()
        'Please add file name and a word as an argument'

    File do not exists:
        >>> sys.argv = [sys.argv[0], 'not_existing_file.txt', 'word']
        >>> main()
        "Can not find the file path: 'not_existing_file.txt'"
    """
    if len(sys.argv) < 3:
        return 'Please add file name and a word as an argument'

    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        return f'Can not find the file path: {file_path!r}'

    word = sys.argv[2]
    with open(file_path, 'r') as rev_f:
        for row in rev_f:
            # rstrip - because we can not add whitespace to doctests
            print(row.rstrip()) if word in row else None


if __name__ == '__main__':
    main()
