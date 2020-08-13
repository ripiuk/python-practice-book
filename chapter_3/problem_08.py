"""
Problem:
    Write a program links.py that takes URL of a webpage as argument and prints
    all the URLs linked from that webpage.
"""

import re
import sys
from urllib.parse import urlparse
from urllib.request import urlopen


def main(url: str) -> None:
    """Download the html from url and print all the linked URLs from it

    Bad URL path:
        >>> main(url='')
        Bad URL path: ''
        >>> main(url='http:/docs.python.org/tutorial/interpreter.html')
        Bad URL path: 'http:/docs.python.org/tutorial/interpreter.html'
        >>> main(url='some text here')
        Bad URL path: 'some text here'
        >>> main(url='ftp://docs.python.org/tutorial/')
        Bad URL path: 'ftp://docs.python.org/tutorial/'

    HTML without links:
        >>> from unittest import mock
        >>> with mock.patch('chapter_3.problem_08.urlopen') as mock_urlopen:
        ...     mock_resp = mock.Mock()
        ...     mock_resp.read.return_value = b'<a href="no url here">Python</a>'
        ...     mock_urlopen.return_value.__enter__.return_value = mock_resp
        ...     main(url='http://not.existing.path')
        <BLANKLINE>

    HTML with https link:
        >>> from unittest import mock
        >>> with mock.patch('chapter_3.problem_08.urlopen') as mock_urlopen:
        ...     mock_resp = mock.Mock()
        ...     mock_resp.read.return_value = b'<a href="https://www.python.org/">Python</a>'
        ...     mock_urlopen.return_value.__enter__.return_value = mock_resp
        ...     main(url='http://not.existing.path')
        https://www.python.org/

    HTML with http link:
        >>> from unittest import mock
        >>> with mock.patch('chapter_3.problem_08.urlopen') as mock_urlopen:
        ...     mock_resp = mock.Mock()
        ...     mock_resp.read.return_value = b'<a href="http://www.python.org/">Python</a>'
        ...     mock_urlopen.return_value.__enter__.return_value = mock_resp
        ...     main(url='http://not.existing.path')
        http://www.python.org/

    HTML with many links:
        >>> from unittest import mock
        >>> with mock.patch('chapter_3.problem_08.urlopen') as mock_urlopen:
        ...     mock_resp = mock.Mock()
        ...     mock_resp.read.return_value = \\
        ...         b'<xmlns="http://some/link1"><href="https://some/link2"/>\\n' \\
        ...         b'<href="http://some/link3"/>'
        ...     mock_urlopen.return_value.__enter__.return_value = mock_resp
        ...     main(url='http://not.existing.path')
        http://some/link1
        https://some/link2
        http://some/link3

    :param url: URL to download.
    :return: None.
    """
    if not (parsed_url := urlparse(url)).scheme \
            or not parsed_url.netloc \
            or parsed_url.scheme not in ('http', 'https'):
        print(f'Bad URL path: {url!r}')
        return

    links = _get_links(url=url)
    print(*links, sep='\n')


def _get_links(url: str) -> list:
    """Download page content and get all the linked URLs from it

    Bad URL:
        >>> _get_links(url='')
        Traceback (most recent call last):
        ...
        ValueError: unknown url type: ''
        >>> _get_links(url='http:/docs.python.org/tutorial/interpreter.html')
        Traceback (most recent call last):
        ...
        urllib.error.URLError: <urlopen error no host given>
        >>> _get_links(url='some text here')
        Traceback (most recent call last):
        ...
        ValueError: unknown url type: 'some text here'

    :param url: page URL to download.
    :return: downloaded file name.
    """
    with urlopen(url) as resp:
        page_content = resp.read().decode('utf-8')
        return re.findall(r'(?<=")(https?[^"]*)', page_content)


if __name__ == "__main__":
    main(url=sys.argv[1])
