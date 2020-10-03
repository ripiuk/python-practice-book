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

### Problem 4
Write a function `treemap` to map a function over nested list.

    >>> treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
    [1, 4, [9, 16, [25]]]

> You can find the solution [here](problem_04.py).

### Problem 5
Write a function `tree_reverse` to reverse elements of a nested-list recursively.

    >>> tree_reverse([[1, 2], [3, [4, 5]], 6])
    [6, [[5, 4], 3], [2, 1]]

> You can find the solution [here](problem_05.py).

### Problem 6
Complete the above implementation of `json_encode` by handling the 
case of dictionaries.

    def json_encode(data):
        if isinstance(data, bool):
            if data:
                return "true"
            else:
                return "false"
        elif isinstance(data, (int, float)):
            return str(data)
        elif isinstance(data, str):
            return '"' + escape_string(data) + '"'
        elif isinstance(data, list):
            return "[" + ", ".join(json_encode(d) for d in data) + "]"
        else:
            raise TypeError("%s is not JSON serializable" % repr(data))
    
    def escape_string(s):
        """Escapes double-quote, tab and new line characters in a string."""
        s = s.replace('"', '\\"')
        s = s.replace("\t", "\\t")
        s = s.replace("\n", "\\n")
        return s

> You can find the solution [here](problem_06.py).

### Problem 7
Implement a program `dirtree.py` that takes a directory as argument 
and prints all the files in that directory recursively as a tree.

Hint: Use `os.listdir` and os.`path.isdir` funtions.

    $ python dirtree.py foo/
    foo/
    |-- a.txt
    |-- b.txt
    |-- bar/
    |   |-- p.txt
    |   `-- q.txt
    `-- c.txt

> You can find the solution [here](problem_07.py).

### Problem 8
Write a function `count_change` to count the number of ways to change 
any given amount. Available coins are also passed as argument to the function.

    >>> count_change(10, [1, 5])
    3
    >>> count_change(10, [1, 2])
    6
    >>> count_change(100, [1, 5, 10, 25, 50])
    292

> You can find the solution [here](problem_08.py).

### Problem 9
Write a function `permute` to compute all possible permutations 
of elements of a given list.

    >>> permute([1, 2, 3])
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

> You can find the solution [here](problem_09.py).
