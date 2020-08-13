"""
Problem:
    Write a regular expression to validate a phone number.

Solution:
    >>> import re
    >>> def is_phone_num_valid(raw_num: str) -> bool:
    ...     return bool(re.match(r'[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\\s\\./0-9]*', raw_num))

    >>> is_phone_num_valid('1234567899')
    True
    >>> is_phone_num_valid('123 456 7899')
    True
    >>> is_phone_num_valid('123-456-7899')
    True
    >>> is_phone_num_valid('(123)-456-7899')
    True
    >>> is_phone_num_valid('(123) 456 7899')
    True
    >>> is_phone_num_valid('(123).456.7899')
    True
    >>> is_phone_num_valid('+380123456789')
    True
    >>> is_phone_num_valid('(012)3456789')
    True
    >>> is_phone_num_valid('(012) 345 6789')
    True
    >>> is_phone_num_valid('(012)-345-6789')
    True
    >>> is_phone_num_valid('(012) 34 56 789')
    True
    >>> is_phone_num_valid('+38(012) 34 56 789')
    True
    >>> is_phone_num_valid('(012)-34-56-789')
    True
    >>> is_phone_num_valid('+38(012)-34-56-789')
    True
    >>> is_phone_num_valid('+38-01-234-56789')
    True
    >>> is_phone_num_valid('some text here')
    False
    >>> is_phone_num_valid(' 1234567899 a')
    False
"""
