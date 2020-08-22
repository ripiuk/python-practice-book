"""
Problem:
    Write a program `myip.py` to print the external IP address of the machine.
    Use the response from `http://httpbin.org/get` and read the IP address from there.
    The program should print only the IP address and nothing else.
"""

import json
import urllib.error
from urllib.request import urlopen


def main() -> None:
    """Get the external IP address of the machine

    Response is not JSON:
        >>> from unittest import mock
        >>> with mock.patch('chapter_3.problem_10.urlopen') as mock_urlopen:
        ...     mock_resp = mock.Mock()
        ...     mock_resp.read.return_value = b'not a JSON'
        ...     mock_urlopen.return_value.__enter__.return_value = mock_resp
        ...     main()
        Can not get the external IP address of the machine. Expecting value: line 1 column 1 (char 0)

    URL Error:
        >>> from unittest import mock
        >>> with mock.patch('chapter_3.problem_10.urlopen') as mock_urlopen:
        ...     mock_resp = mock.Mock()
        ...     mock_resp.read.side_effect = urllib.error.URLError(reason='test_err')
        ...     mock_urlopen.return_value.__enter__.return_value = mock_resp
        ...     main()
        Can not get the external IP address of the machine. <urlopen error test_err>

    Unexpected response format:
        >>> from unittest import mock
        >>> with mock.patch('chapter_3.problem_10.urlopen') as mock_urlopen:
        ...     mock_resp = mock.Mock()
        ...     mock_resp.read.return_value = b'{"not_origin": "192.168.1.1", "url": "http://test.url"}'
        ...     mock_urlopen.return_value.__enter__.return_value = mock_resp
        ...     main()
        Can not find IP address in the response: {'not_origin': '192.168.1.1', 'url': 'http://test.url'}

    Expected response format:
        >>> from unittest import mock
        >>> with mock.patch('chapter_3.problem_10.urlopen') as mock_urlopen:
        ...     mock_resp = mock.Mock()
        ...     mock_resp.read.return_value = b'{"origin": "192.168.1.1", "url": "http://test.url"}'
        ...     mock_urlopen.return_value.__enter__.return_value = mock_resp
        ...     main()
        Your IP address: 192.168.1.1

    :return: None.
    """
    try:
        with urlopen('http://httpbin.org/get') as resp:
            page_content: dict = json.loads(resp.read().decode('utf-8'))
            if ip := page_content.get('origin'):
                print('Your IP address:', ip)
                return
            print('Can not find IP address in the response:', page_content)
    except (json.JSONDecodeError, ValueError, urllib.error.URLError) as err:
        print('Can not get the external IP address of the machine.', err)


if __name__ == "__main__":
    main()
