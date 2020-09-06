## 5. Iterators & Generators

### Problem 1
Write an iterator class `reverse_iter`, that takes a list and iterates 
it from the reverse direction.

    >>> it = reverse_iter([1, 2, 3, 4])
    >>> next(it)
    4
    >>> next(it)
    3
    >>> next(it)
    2
    >>> next(it)
    1
    >>> next(it)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

> You can find the solution [here](problem_01.py).

### Problem 2
Write a program that takes one or more filenames as arguments 
and prints all the lines which are longer than 40 characters.

> You can find the solution [here](problem_02.py).

### Problem 3
Write a function `findfiles` that recursively descends the directory tree 
for the specified directory and generates paths of all the files in the tree.

> You can find the solution [here](problem_03.py).

### Problem 4
Write a function to compute the number of python files (.py extension) 
in a specified directory recursively.

> You can find the solution [here](problem_04.py).

### Problem 5
Write a function to compute the total number of lines of code in all 
python files in the specified directory recursively.

> You can find the solution [here](problem_05.py).

### Problem 6
Write a function to compute the total number of lines of code, 
ignoring empty and comment lines, in all python files in the 
specified directory recursively.

> You can find the solution [here](problem_06.py).

### Problem 7
Write a program `split.py`, that takes an integer `n` and a filename 
as command line arguments and splits the file into multiple small files 
with each having `n` lines.

> You can find the solution [here](problem_07.py).

### Problem 8
Write a function `peep`, that takes an iterator as argument 
and returns the first element and an equivalent iterator.

    >>> it = iter(range(5))
    >>> x, it1 = peep(it)
    >>> print(x, list(it1))
    0 [0, 1, 2, 3, 4]

> You can find the solution [here](problem_08.py).

### Problem 9
The built-in function `enumerate` takes an iteratable and returns 
an iterator over pairs (index, value) for each value in the source.

    >>> list(enumerate(["a", "b", "c"]))
    [(0, "a"), (1, "b"), (2, "c")]
    >>> for i, c in enumerate(["a", "b", "c"]):
    ...     print(i, c)
    ...
    0 a
    1 b
    2 c

Write a function `my_enumerate` that works like `enumerate`.

> You can find the solution [here](problem_09.py).

### Problem 10
Implement a function `izip` that works like `itertools.izip` 
(equivalent to Python3 built-in `zip` function).

> You can find the solution [here](problem_10.py).
