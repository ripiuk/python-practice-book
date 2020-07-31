"""
Problem:
    Write a python function `parse_csv` to parse csv (comma separated values) files.

Solution:
    >>> import tempfile
    >>> import typing as typ
    >>> def parse_csv(file_path: str) -> typ.List[typ.List[str]]:
    ...     with open(file_path, 'r') as file:
    ...         return [line.rstrip().split(',') for line in file]

    >>> file_content = 'a,b,c\\n1,2,3\\n2,3,4\\n3,4,5'
    >>> with tempfile.NamedTemporaryFile() as tmp_f:
    ...     _ = tmp_f.write(file_content.encode())
    ...     _ = tmp_f.seek(0)
    ...     parse_csv(tmp_f.name)
    [['a', 'b', 'c'], ['1', '2', '3'], ['2', '3', '4'], ['3', '4', '5']]
"""
