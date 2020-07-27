"""
Problem:
    Write a program to print each line of a file in reverse order.

Example:
    $ cat she.txt
    She sells seashells on the seashore;
    The shells that she sells are seashells I'm sure.
    So if she sells seashells on the seashore,
    I'm sure that the shells are seashore shells.

    $ python chapter_2/problem_18.py she.txt
    ;erohsaes eht no sllehsaes slles ehS
    .erus m'I sllehsaes era slles ehs taht sllehs ehT
    ,erohsaes eht no sllehsaes slles ehs fi oS
    .sllehs erohsaes era sllehs eht taht erus m'I
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
    ;erohsaes eht no sllehsaes slles ehS
    .erus m'I sllehsaes era slles ehs taht sllehs ehT
    ,erohsaes eht no sllehsaes slles ehs fi oS
    .sllehs erohsaes era sllehs eht taht erus m'I

    No arguments provided
    >>> sys.argv = sys.argv[:1]
    >>> main()
    'Please add file name as an argument'

    File do not exists
    >>> sys.argv = [sys.argv[0], 'not_existing_file.txt']
    >>> main()
    "Can not find the file path: 'not_existing_file.txt'"
    """
    if len(sys.argv) <= 1:
        return 'Please add file name as an argument'

    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        return f'Can not find the file path: {file_path!r}'

    with open(file_path, 'r') as rev_f:
        for line in rev_f:
            print(line.rstrip()[::-1])  # rstrip - because we can not add whitespace to doctests


if __name__ == '__main__':
    main()
