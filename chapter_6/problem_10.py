"""
Problem:
    Write a function `profile`, which takes a function as argument and returns
    a new function, which behaves exactly similar to the given function,
    except that it prints the time consumed in executing it.
"""

import time
import typing as typ
from functools import wraps


def profile(fn: typ.Callable) -> typ.Callable:
    """Decorator that prints the time consumed in executing
    for the given function

    Tests:
        >>> from functools import lru_cache
        >>> @lru_cache(maxsize=128)
        ... def fib(n: int) -> int:
        ...     return 1 if n in {0, 1} else fib(n - 1) + fib(n - 2)
        >>> smt = profile(fib)
        >>> smt(20)
        time taken: 0... sec
        10946

        >>> profile(fn=lambda: time.sleep(0.2))()
        time taken: 0.2... sec
        None

    :param fn: function
    :return: decorated function
    """
    @wraps(fn)
    def wrap(*args, **kwargs):
        start = time.time()
        res = fn(*args, **kwargs)
        print(
            f'time taken: {time.time() - start:2.4f} sec\n'
            f'{res}'
        )
    return wrap
