## 6. Functional Programming

### Problem 1
Implement a function `product` to multiply 2 numbers recursively 
using `+` and `-` operators only.

> You can find the solution [here](problem_01.py).

### Problem 2
Write a function `flatten_dict` to flatten a nested dictionary 
by joining the keys with `.` character.

    >>> flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
    {'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}

> You can find the solution [here](problem_02.py).

### Problem 3
Write a function `unflatten_dict` to do reverse of `flatten_dict`.

    >>> unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
    {'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}

> You can find the solution [here](problem_03.py).
