"""
Problem:
    Write a program `wget.py` to download a given URL.
    The program should accept a URL as argument, download it and save it
    with the basename of the URL. If the URL ends with a `/`, consider
    the basename as `index.html`. (Using `urllib` module)

Example:
    $ python wget.py http://docs.python.org/tutorial/interpreter.html
    saving http://docs.python.org/tutorial/interpreter.html as interpreter.html.

    $ python wget.py http://docs.python.org/tutorial/
    saving http://docs.python.org/tutorial/ as index.html.
"""

import re
import sys
from pathlib import Path
from unittest import mock
from urllib.parse import urlparse
from urllib.request import urlopen


def main(url: str) -> None:
    """Download a given URL

    Bad URL path:
        >>> main(url='')
        Bad URL path: ''
        >>> main(url='http:/docs.python.org/tutorial/interpreter.html')
        Bad URL path: 'http:/docs.python.org/tutorial/interpreter.html'
        >>> main(url='some text here')
        Bad URL path: 'some text here'
        >>> main(url='ftp://docs.python.org/tutorial/')
        Bad URL path: 'ftp://docs.python.org/tutorial/'

    Download page with a file name inside the URL:
        >>> from pathlib import Path
        >>> file_path = Path('test_problem_05_download_page.html')
        >>> try:
        ...     with mock.patch('chapter_3.problem_05.urlopen') as mock_urlopen:
        ...         mock_resp = mock.Mock()
        ...         mock_resp.read.return_value = b'test content'
        ...         mock_urlopen.return_value.__enter__.return_value = mock_resp
        ...         main(url=f'http://not.existing.path/{file_path.name}')
        ...     print(file_path.read_text())
        ... finally:
        ...     file_path.unlink()
        Saved 'http://not.existing.path/test_problem_05_download_page.html' as 'test_problem_05_download_page.html'
        test content

    :param url: URL to download.
    :return: None.
    """
    if not (parsed_url := urlparse(url)).scheme \
            or not parsed_url.netloc \
            or parsed_url.scheme not in ('http', 'https'):
        print(f'Bad URL path: {url!r}')
        return

    file_name = _get_file_name(url_path=parsed_url.path)
    _download_page(url=url, file_name=file_name)
    print(f'Saved {url!r} as {file_name!r}')


def _get_file_name(url_path: str) -> str:
    """Get file name from the basename of the URL

    URL without file name:
        >>> _get_file_name(url_path='/no/file/here')
        'index.html'
        >>> _get_file_name(url_path='/test.')
        'index.html'
        >>> _get_file_name(url_path='/.test')
        'index.html'

    URLs with file name:
        >>> _get_file_name(url_path='/tutorial/interpreter.html')
        'interpreter.html'
        >>> _get_file_name(url_path='path/test.txt')
        'test.txt'
        >>> _get_file_name(url_path='/test.a')
        'test.a'

    :param url_path: url path. e.g: '/tutorial/interpreter.html'.
    :return: file name from the basename of the URL. Defaults to 'index.html'.
    """
    return file_name \
        if re.match(
            pattern=r'^[\w,\s-]+\.[\w]+$',
            string=(file_name := Path(url_path).name),
        ) \
        else 'index.html'


def _download_page(url: str, file_name: str) -> None:
    """Download page content and save it with the basename of the URL

    Bad URL:
        >>> _download_page(url='', file_name='')
        Traceback (most recent call last):
        ...
        ValueError: unknown url type: ''
        >>> _download_page(
        ...     url='http:/docs.python.org/tutorial/interpreter.html',
        ...     file_name='',
        ... )
        Traceback (most recent call last):
        ...
        urllib.error.URLError: <urlopen error no host given>
        >>> _download_page(url='some text here', file_name='')
        Traceback (most recent call last):
        ...
        ValueError: unknown url type: 'some text here'

    Download page:
        >>> import tempfile
        >>> with tempfile.NamedTemporaryFile() as tmp_f:
        ...     with mock.patch('chapter_3.problem_05.urlopen') as mock_urlopen:
        ...         mock_resp = mock.Mock()
        ...         mock_resp.read.return_value = b'test content'
        ...         mock_urlopen.return_value.__enter__.return_value = mock_resp
        ...         _download_page(url='http://not.existing.path', file_name=tmp_f.name)
        ...     with open(tmp_f.name, 'r') as res_f:
        ...         print(res_f.read())
        test content

    :param url: page URL to download.
    :param file_name: file name
    :return: downloaded file name.
    """
    with urlopen(url) as resp, open(file_name, 'wb') as res_f:
        res_f.write(resp.read())


if __name__ == "__main__":
    main(url=sys.argv[1])
