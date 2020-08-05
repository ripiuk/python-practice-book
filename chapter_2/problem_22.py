"""
Problem:
    The previous wrap program is not so nice because
    it is breaking the line at middle of any word.
    Can you write a new program wordwrap.py that works
    like wrap.py, but breaks the line only at the word boundaries?

Example:
    $ cat she.txt
    She sells seashells on the seashore;
    The shells that she sells are seashells I'm sure.
    So if she sells seashells on the seashore,
    I'm sure that the shells are seashore shells.

    $ python chapter_2/problem_22.py she.txt 30
    She sells seashells on the
    seashore;
    The shells that she sells are
    seashells I'm sure.
    So if she sells seashells on
    the seashore,
    I'm sure that the shells are
    seashore shells.
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
        ...     sys.argv = [sys.argv[0], tmp_f.name, '30']
        ...     main()
        She sells seashells on the
        seashore;
        The shells that she sells are
        seashells I'm sure.
        So if she sells seashells on
        the seashore,
        I'm sure that the shells are
        seashore shells.

    Check the function with long words:
        >>> file_content = '''Some text here and longlonglonglonglonglonglonglonglonglonglonglonglong word
        ... And also in the next row longlonglonglonglonglonglonglonglonglonglonglonglonglonglong word'''
        >>> import tempfile
        >>> with tempfile.NamedTemporaryFile() as tmp_f:
        ...     _ = tmp_f.write(file_content.encode())
        ...     _ = tmp_f.seek(0)
        ...     sys.argv = [sys.argv[0], tmp_f.name, '30']
        ...     main()
        Some text here and
        longlonglonglonglonglonglonglo
        nglonglonglonglonglong word
        And also in the next row
        longlonglonglonglonglonglonglo
        nglonglonglonglonglonglonglong
        word

    No arguments provided:
        >>> sys.argv = sys.argv[:1]
        >>> main()
        'Please add file name and width as an argument'

    No width argument provided:
        >>> sys.argv = [sys.argv[0], 'some_file.txt']
        >>> main()
        'Please add file name and width as an argument'

    File do not exists:
        >>> sys.argv = [sys.argv[0], 'not_existing_file.txt', '10']
        >>> main()
        "Can not find the file path: 'not_existing_file.txt'"

    Width is not integer:
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
            for part in split_row(row, width):
                print(part)


def split_row(row: str, width: int):
    i = 0
    left = row
    while left:
        curr_width = width
        part = row[i:i+curr_width]
        if len(part) >= width:
            for j, letter in enumerate(part[::-1]):
                if letter == ' ':
                    part = part[:len(part)-j]
                    curr_width = len(part)
                    break
        # rstrip - because we can not add whitespace to doctests
        yield part.rstrip().lstrip()
        i += curr_width
        left = left[curr_width:]


if __name__ == '__main__':
    main()
