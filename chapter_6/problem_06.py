"""
Problem:
    Complete the above implementation of `json_encode` by handling the case of dictionaries.
"""

import typing as typ


def json_encode(data: typ.Any) -> str:
    """Serialize python object to a JSON formatted string.

    Tests:
        >>> import json
        >>> samples = (
        ...     # str
        ...     'some text',
        ...     'text with "quote"',
        ...     'with \t',
        ...     'with \\n',
        ...
        ...     # bool
        ...     True,
        ...     False,
        ...
        ...     # int
        ...     1,
        ...     123435509,
        ...     -2137,
        ...
        ...     # float
        ...     0.0,
        ...     1.2,
        ...     -5.9,
        ...
        ...     # list
        ...     [1, '2', 3.0, [4, 5]],
        ...
        ...     # dict
        ...     {1: True, '2': 1.0, 'nested': {'key': [1, 2, {'key': 'value'}]}},
        ... )
        >>> for sample in samples:
        ...     if (result := json_encode(sample)) != (expected := json.dumps(sample)):
        ...         print(f'{result!r} != {expected!r}')

    :param data: python object
    :return: json string
    """
    cls_encode = {
        str: lambda x: '"{}"'.format(
            data.replace('"', '\\"')
                .replace("\t", "\\t")
                .replace("\n", "\\n")
        ),
        bool: lambda x: "true" if x else "false",
        int: lambda x: str(x),
        float: lambda x: str(x),
        list: lambda x: f'[{", ".join(json_encode(el) for el in x)}]',
        dict: lambda x:
            f'{{{", ".join(f"{json_encode(str(k))}: {json_encode(v)}" for k, v in x.items())}}}',
    }

    encode_func = cls_encode.get(type(data))
    if not encode_func:
        raise TypeError(f'{data!r} is not JSON serializable')

    return encode_func(data)
