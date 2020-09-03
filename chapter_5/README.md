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
