## 3. Modules

### Problem 1
Write a program to list all files in the given directory.

> You can find the solution [here](problem_01.py).

### Problem 2
Write a program `extcount.py` to count number of files for each extension 
in the given directory. The program should take a directory name 
as argument and print count and extension for each available file extension.

    $ python extcount.py src/
    14 py
    4 txt
    1 csv

> You can find the solution [here](problem_02.py).

### Problem 3
Write a program to list all the files in the given directory 
along with their length and last modification time. 
The output should contain one line for each file containing filename, 
length and modification date separated by tabs.

Hint: see help for `os.stat`.

> You can find the solution [here](problem_03.py).

### Problem 4
Write a program to print directory tree. The program should take path of a directory 
as argument and print all the files in it recursively as a tree.

    $ python dirtree.py foo
    foo
    |-- a.txt
    |-- b.txt
    |-- code
    |   |-- a.py
    |   |-- b.py
    |   |-- docs
    |   |   |-- a.txt
    |   |   \-- b.txt
    |   \-- x.py
    \-- z.txt

> You can find the solution [here](problem_04.py).
