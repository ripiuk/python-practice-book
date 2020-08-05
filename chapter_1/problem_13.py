"""
Problem:
    Write a program `add.py` that takes 2 numbers as command line arguments and prints its sum.

Example:
    $ python chapter_1/problem_13.py 3 5
    8
    $ python chapter_1/problem_13.py 2 9
    11
"""

import sys


def main():
    """
    Check the function with the data from the example above:
        >>> sys.argv = [sys.argv[0], '3', '5']
        >>> main()
        8
        >>> sys.argv = [sys.argv[0], '2', '9']
        >>> main()
        11

    No arguments provided:
        >>> sys.argv = sys.argv[:1]
        >>> main()
        Please provide some arguments.

    Got strings instead of integers:
        >>> sys.argv = [sys.argv[0], '2', 'string']
        >>> main()
        Error: All the arguments should be integers

    Many arguments:
        >>> sys.argv = [sys.argv[0], '1', '2', '3', '4', '5']
        >>> main()
        15
    """
    if len(sys.argv) <= 1:
        print('Please provide some arguments.')
        return

    numbers = sys.argv[1:]
    if any(not number.isdigit() for number in numbers):
        print('Error: All the arguments should be integers')
        return

    print(sum(map(int, numbers)))


if __name__ == '__main__':
    main()
