"""
Problem:
    Implement unix commands `head` and `tail`.
    The `head` and `tail` commands take a file as argument
    and prints its first and last 10 lines of the file respectively.

Example:
    $ cat she.txt
    She sells seashells on the seashore;
    The shells that she sells are seashells I'm sure.
    So if she sells seashells on the seashore,
    I'm sure that the shells are seashore shells.

    $ python chapter_2/problem_19.py head she.txt 2
    She sells seashells on the seashore;
    The shells that she sells are seashells I'm sure.

    $ python chapter_2/problem_19.py tail she.txt 3
    The shells that she sells are seashells I'm sure.
    So if she sells seashells on the seashore,
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
        ...     sys.argv = [sys.argv[0], 'head', tmp_f.name, 2]
        ...     main()
        She sells seashells on the seashore;
        The shells that she sells are seashells I'm sure.

        >>> with tempfile.NamedTemporaryFile() as tmp_f:
        ...     _ = tmp_f.write(file_content.encode())
        ...     _ = tmp_f.seek(0)
        ...     sys.argv = [sys.argv[0], 'tail', tmp_f.name, 3]
        ...     main()
        The shells that she sells are seashells I'm sure.
        So if she sells seashells on the seashore,
        I'm sure that the shells are seashore shells.

    No arguments provided:
        >>> sys.argv = sys.argv[:1]
        >>> main()
        'Please add method (head or tail) and file name as an argument'

    No file argument provided:
        >>> sys.argv = [sys.argv[0], 'tail']
        >>> main()
        'Please add method (head or tail) and file name as an argument'

    Bad method name:
        >>> sys.argv = [sys.argv[0], 'bad_method', 'not_existing_file.txt']
        >>> main()
        'Wrong method name'

    Bad limit value:
        >>> sys.argv = [sys.argv[0], 'head', sys.argv[0], 'bad_limit']
        >>> main()
        "Got bad limit value: 'bad_limit'"

    File do not exists:
        >>> sys.argv = [sys.argv[0], 'head', 'not_existing_file.txt']
        >>> main()
        "Can not find the file path: 'not_existing_file.txt'"
    """
    methods = {
        'head': _print_head,
        'tail': _print_tail,
    }

    if len(sys.argv) < 3:
        return 'Please add method (head or tail) and file name as an argument'

    method = sys.argv[1]
    if method not in methods:
        return 'Wrong method name'

    file_path = sys.argv[2]
    if not os.path.exists(file_path):
        return f'Can not find the file path: {file_path!r}'

    limit = sys.argv[3] if len(sys.argv) >= 3 else 10
    if isinstance(limit, str):
        if not limit.isdigit():
            return f'Got bad limit value: {limit!r}'
        limit = int(limit)

    with open(file_path, 'r') as rev_f:
        for row in methods[method](file=rev_f, limit=limit):
            print(row)


def _print_head(file, limit: int):
    for row_num, row in enumerate(file):
        if row_num >= limit:
            break
        yield row.rstrip()  # rstrip - because we can not add whitespace to doctests


def _print_tail(file, limit: int):
    lines = file.readlines()
    for row in lines[len(lines) - limit:]:
        yield row.rstrip()  # rstrip - because we can not add whitespace to doctests


if __name__ == '__main__':
    main()
