"""
Problem:
    Create a new virtualenv and install BeautifulSoup.
    BeautifulSoup is very good library for parsing HTML.
    Try using it to extract all HTML links from a webpage.

Solution:
    Using BeautifulSoup:
        >>> from bs4 import BeautifulSoup, SoupStrainer
        >>> def bs4_get_links(html_page: str) -> list:
        ...     return [
        ...         link['href']
        ...         for link in BeautifulSoup(html_page, 'html.parser', parse_only=SoupStrainer('a'))
        ...         if link.has_attr('href')
        ...     ]

        >>> bs4_get_links('<a href="http://test.link/example.html">посилання</a>')
        ['http://test.link/example.html']
        >>> bs4_get_links('<a href="http://test.link"></a>\\n\\n<a href="http://test.link2"></a>')
        ['http://test.link', 'http://test.link2']

    Using lxml:
        >>> import lxml.html
        >>> def lxml_get_links(html_page: str) -> list:
        ...     return [link for link in lxml.html.fromstring(html_page).xpath('//a/@href')]

        >>> lxml_get_links('<a href="http://test.link/example.html">посилання</a>')
        ['http://test.link/example.html']
        >>> lxml_get_links('<a href="http://test.link"></a>\\n\\n<a href="http://test.link2"></a>')
        ['http://test.link', 'http://test.link2']
"""
