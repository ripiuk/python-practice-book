"""
Problem:
    Write a program `antihtml.py` that takes a URL as argument, downloads the html from
    web and print it after stripping html tags using regex.

Example:
    $ python antihtml.py index.html
    ...
    The Python interpreter is usually installed as /usr/local/bin/python on
    those machines where it is available; putting /usr/local/bin in your
    ...
"""

import re
import sys
from unittest import mock
from urllib.parse import urlparse
from urllib.request import urlopen


def main(url: str) -> None:
    """Download the html from url and print it after stripping html tags

    Bad URL path:
        >>> main(url='')
        Bad URL path: ''
        >>> main(url='http:/docs.python.org/tutorial/interpreter.html')
        Bad URL path: 'http:/docs.python.org/tutorial/interpreter.html'
        >>> main(url='some text here')
        Bad URL path: 'some text here'
        >>> main(url='ftp://docs.python.org/tutorial/')
        Bad URL path: 'ftp://docs.python.org/tutorial/'

    Text without html tags:
        >>> with mock.patch('chapter_3.problem_06.urlopen') as mock_urlopen:
        ...     mock_resp = mock.Mock()
        ...     mock_resp.read.return_value = b'content without html tags'
        ...     mock_urlopen.return_value.__enter__.return_value = mock_resp
        ...     main(url='http://not.existing.path')
        content without html tags

    Strip html tags:
        >>> with mock.patch('chapter_3.problem_06.urlopen') as mock_urlopen:
        ...     mock_resp = mock.Mock()
        ...     mock_resp.read.return_value = b'<html>test content</html>'
        ...     mock_urlopen.return_value.__enter__.return_value = mock_resp
        ...     main(url='http://not.existing.path')
        test content

    Strip html tags with a new line inside
        >>> with mock.patch('chapter_3.problem_06.urlopen') as mock_urlopen:
        ...     mock_resp = mock.Mock()
        ...     mock_resp.read.return_value = b'<link rel="search" \\n  title="Python 3.8.5" \\n href="../>'
        ...     mock_urlopen.return_value.__enter__.return_value = mock_resp
        ...     main(url='http://not.existing.path')
        <BLANKLINE>

    :param url: URL to download.
    :return: None.
    """
    if not (parsed_url := urlparse(url)).scheme \
            or not parsed_url.netloc \
            or parsed_url.scheme not in ('http', 'https'):
        print(f'Bad URL path: {url!r}')
        return

    text = _strip_page(url=url)
    print(text)


def _strip_page(url: str) -> str:
    """Download page content and strip html tags from it

    Bad URL:
        >>> _strip_page(url='')
        Traceback (most recent call last):
        ...
        ValueError: unknown url type: ''
        >>> _strip_page(url='http:/docs.python.org/tutorial/interpreter.html')
        Traceback (most recent call last):
        ...
        urllib.error.URLError: <urlopen error no host given>
        >>> _strip_page(url='some text here')
        Traceback (most recent call last):
        ...
        ValueError: unknown url type: 'some text here'

    :param url: page URL to download.
    :return: downloaded file name.
    """
    with urlopen(url) as resp:
        page_content = resp.read().decode('utf-8')
        return '\n'.join(
            line
            for raw_line in re.sub(r'<[^<]+?>', '', page_content).split('\n')
            if (line := raw_line.strip())
        )


if __name__ == "__main__":
    main(url=sys.argv[1])
