## 1. Getting Started

### Problem 1
Open a new Python interpreter and use it to find the value of `2 + 3`.

> You can find the solution [here](problem_01.py).

### Problem 2
How many multiplications are performed when each of the following lines 
of code is executed?

    print square(5)
    print square(2*5)

> You can find the solution [here](problem_02.py).

### Problem 3
What will be the output of the following program?

    x = 1
    def f():
        return x
    print(x)
    print(f())

> You can find the solution [here](problem_03.py).

### Problem 4
What will be the output of the following program?

    x = 1
    def f():
        x = 2
        return x
    print(x)
    print(f())
    print(x)

> You can find the solution [here](problem_04.py).

### Problem 5
What will be the output of the following program?

    x = 1
    def f():
        y = x
        x = 2
        return x + y
    print(x)
    print(f())
    print(x)

> You can find the solution [here](problem_05.py).

### Problem 6
What will be the output of the following program?

    x = 2
    def f(a):
        x = a * a
        return x
    y = f(3)
    print(x, y)

> You can find the solution [here](problem_06.py).

### Problem 7
Write a function `count_digits` to find number of digits 
in the given number.

    >>> count_digits(5)
    1
    >>> count_digits(12345)
    5

> You can find the solution [here](problem_07.py).

### Problem 8
Write a function istrcmp to compare two strings, ignoring the case.

    >>> istrcmp('python', 'Python')
    True
    >>> istrcmp('LaTeX', 'Latex')
    True
    >>> istrcmp('a', 'b')
    False

> You can find the solution [here](problem_08.py).

### Problem 9
What will be output of the following program?

    print(2 < 3 and 3 > 1)
    print(2 < 3 or 3 > 1)
    print(2 < 3 or not 3 > 1)
    print(2 < 3 and not 3 > 1)

> You can find the solution [here](problem_09.py)

### Problem 10
What will be output of the following program?

    x = 4
    y = 5
    p = x < y or x < z
    print(p)

> You can find the solution [here](problem_10.py)

### Problem 11
What happens when the following code is executed? Will it give any error? 
Explain the reasons.

    x = 2
    if x == 2:
        print(x)
    else:
        print(y)

> You can find the solution [here](problem_11.py)

### Problem 12
What happens the following code is executed? Will it give any error? 
Explain the reasons.

    x = 2
    if x == 2:
        print(x)
    else:
        x +

> You can find the solution [here](problem_12.py)

### Problem 13
Write a program `add.py` that takes 2 numbers as command line 
arguments and prints its sum.

    $ python add.py 3 5
    8
    $ python add.py 2 9
    11

> You can find the solution [here](problem_13.py)
