"""
Problem:
    Write a function make_slug that takes a name converts it into a slug.
    A slug is a string where spaces and special characters are replaced by a hyphen,
    typically used to create blog post URL from post title. It should also make sure
    there are no more than one hyphen in any place and there are no hyphens at the
    biginning and end of the slug.

Solution:
    >>> import re
    >>> def make_slug(raw_word: str) -> str:
    ...     transliteration = {
    ...         'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e',
    ...         'є': 'ie', 'ж': 'zh', 'з': 'z', 'и': 'y', 'і': 'i', 'ї': 'i', 'й': 'i',
    ...         'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
    ...         'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch',
    ...         'ш': 'sh', 'щ': 'shch', 'ь': '_', 'ю': 'iu', 'я': 'ia'}
    ...     transliteration = {ord(k): v for k, v in transliteration.items()}
    ...     return re.sub(
    ...         pattern=r'[-\\s]+',
    ...         repl='-',
    ...         string=re.sub(
    ...             pattern=r'[^\\w\\s]',
    ...             repl='',
    ...             string=raw_word,
    ...         ).strip().lower(),
    ...     ).translate(transliteration)

    >>> make_slug("hello world")
    'hello-world'
    >>> make_slug("hello  world!")
    'hello-world'
    >>> make_slug(" --hello-  world--")
    'hello-world'
    >>> make_slug(" Привіт -- - ! Світе")
    'pryvit-svite'
"""
