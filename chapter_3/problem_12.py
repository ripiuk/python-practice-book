"""
Problem:
    Write a program `mydoc.py` to implement the functionality of `pydoc`.
    The program should take the module name as argument and print documentation
    for the module and each of the functions defined in that module.

Example:
    $ python mydoc.py os
    Help on module os:

    DESCRIPTION

    os - OS routines for Mac, NT, or Posix depending on what system we're on.
    ...

    FUNCTIONS

    getcwd()
        ...
"""


import sys
import pydoc
import inspect


def main(module_name: str) -> None:
    """Get module documentation

    Unknown module name:
        >>> main('unknown module')
        Can not find module 'unknown module'!

    Get documentation for `os` module:
        >>> main('os')
        Help on module os:
        ...
        DESCRIPTION
        ...
        OS routines for NT or Posix depending on what system we're on.
        ...
        FUNCTIONS
        ...
        getenv(key, default=None)
        ...

    :param module_name: module name.
    :return: None.
    """
    module = pydoc.safeimport(module_name)
    if module is None:
        print(f'Can not find module {module_name!r}!')
        return

    print(
        f'Help on module {module_name}:\n\n'
        f'DESCRIPTION\n\n'
        f'{module.__doc__}\n'
    )

    print('FUNCTIONS\n')
    for func in inspect.getmembers(module, inspect.isfunction):
        print(f'{func[0]}{inspect.signature(func[1])}')
        print('\n'.join(f'\t{row}' for row in func_doc.split('\n')), '\n') \
            if (func_doc := inspect.getdoc(func[1])) \
            else print()


if __name__ == "__main__":
    main(sys.argv[1])
