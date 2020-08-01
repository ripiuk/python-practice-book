"""
Problem:
    Write a program to count frequency of characters in a given file.
    Can you use character frequency to tell whether the given file is a
    Python program file, C program file or a text file?
"""

import tempfile
from pathlib import Path
from collections import Counter


def chars_frequency(filename: str) -> Counter:
    """Get words from a file

    Example:
        >>> file_content = '1 line\\n2 line'
        >>> with tempfile.NamedTemporaryFile() as tmp_f:
        ...     _ = tmp_f.write(file_content.encode())
        ...     _ = tmp_f.seek(0)
        ...     chars_frequency(tmp_f.name)
        Counter({' ': 2, 'l': 2, 'i': 2, 'n': 2, 'e': 2, '1': 1, '\\n': 1, '2': 1})

    :param filename: path to a local file
    :return: sequence of words from the file
    """
    return Counter(Path(filename).read_text())


def main(filename: str) -> None:
    """Entry point

    Example:
        >>> file_content = 'first line\\nsecond line'
        >>> with tempfile.NamedTemporaryFile() as tmp_f:
        ...     _ = tmp_f.write(file_content.encode())
        ...     _ = tmp_f.seek(0)
        ...     main(tmp_f.name)
        'i' 3
        'n' 3
        'e' 3
        's' 2
        ' ' 2
        'l' 2
        'f' 1
        'r' 1
        't' 1
        '\\n' 1
        File extension by its content: .txt

    :param filename: path to a local file
    :return: None
    """
    frequency = chars_frequency(filename)
    for word, count in frequency.most_common(10):
        print(f'{word!r}', count, flush=True)
    print('File extension by its content:', file_extension_suggestion(frequency))


def file_extension_suggestion(frequency: Counter) -> str:
    """Suggest file extension by chars frequency

    Example:
        >>> file_extension_suggestion(Counter('''#include <iostream>
        ...     int main() {
        ...         std::cout << "Hello World!";
        ...         return 0;
        ...     }'''))
        '.c'
        >>> file_extension_suggestion(Counter('''def main():
        ...     print("Hello World!")
        ...     if __name__== "__main__":
        ...     main()'''))
        '.py'
        >>> file_extension_suggestion(Counter('some text here'))
        '.txt'


    :param frequency: the frequency of chars
    :return: suggested file extension
    """
    extensions = {
        '.c': lambda fqc: (
                any('n' in char for char, _ in fqc.most_common(10))
                and ';' in fqc
        ),
        '.py': lambda fqc: (
                any('e' in char for char, _ in fqc.most_common(10))
                and ';' not in fqc
                and fqc.most_common(1)
                and ' ' == fqc.most_common(1)[0][0]
        ),
    }
    for ext, condition in extensions.items():
        if condition(frequency):
            return ext
    return '.txt'


if __name__ == "__main__":
    import sys
    main(sys.argv[1])
