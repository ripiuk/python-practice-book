"""
Problem:
    Generalize the above (problem_30) implementation of csv parser
    to support any delimiter and comments.

Solution:
    >>> import tempfile
    >>> import typing as typ
    >>> def parse_csv(file_path: str, sep: str = ',', comment_sign: str = '#') -> typ.List[typ.List[str]]:
    ...     with open(file_path, 'r') as file:
    ...         return [line.rstrip().split(sep) for line in file if comment_sign not in line]

    >>> file_content = '# elements are separated by ! and comment indicator is #\\na!b!c\\n1!2!3\\n2!3!4\\n3!4!5'
    >>> with tempfile.NamedTemporaryFile() as tmp_f:
    ...     _ = tmp_f.write(file_content.encode())
    ...     _ = tmp_f.seek(0)
    ...     parse_csv(tmp_f.name, '!', '#')
    [['a', 'b', 'c'], ['1', '2', '3'], ['2', '3', '4'], ['3', '4', '5']]
"""
