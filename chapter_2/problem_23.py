"""
Problem:
    Write a program center_align.py to center align all lines in the given file.

Example:
    $ cat she.txt
    She sells seashells on the seashore;
    The shells that she sells are seashells I'm sure.
    So if she sells seashells on the seashore,
    I'm sure that the shells are seashore shells.

    $ python chapter_2/problem_23.py she.txt
           She sells seashells on the seashore;
    The shells that she sells are seashells I'm sure.
        So if she sells seashells on the seashore,
      I'm sure that the shells are seashore shells.
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
    ...     sys.argv = [sys.argv[0], tmp_f.name]
    ...     main()
          She sells seashells on the seashore;
    The shells that she sells are seashells I'm sure.
       So if she sells seashells on the seashore,
      I'm sure that the shells are seashore shells.

    No arguments provided
    >>> sys.argv = sys.argv[:1]
    >>> main()
    'Please add file name as an argument'

    File do not exists
    >>> sys.argv = [sys.argv[0], 'not_existing_file.txt']
    >>> main()
    "Can not find the file path: 'not_existing_file.txt'"
    """
    if len(sys.argv) < 2:
        return 'Please add file name as an argument'

    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        return f'Can not find the file path: {file_path!r}'

    with open(file_path, 'r') as rev_f:
        rows = [row.strip() for row in rev_f]
        max_width = max(map(len, rows))
        # Another option, but we can not add whitespace to doctests, so it fails:
        # print('\n'.join(f'{row:^{max_width}}' for row in rows))
        for row in rows:
            # rstrip - because we can not add whitespace to doctests
            print(f'{row:^{max_width}}'.rstrip())


if __name__ == '__main__':
    main()
