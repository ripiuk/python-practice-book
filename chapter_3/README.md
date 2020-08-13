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

### Problem 5
Write a program `wget.py` to download a given URL. 
The program should accept a URL as argument, download it and save it 
with the basename of the URL. If the URL ends with a `/`, consider 
the basename as `index.html`. (Using `urllib` module)

    $ python wget.py http://docs.python.org/tutorial/interpreter.html
    saving http://docs.python.org/tutorial/interpreter.html as interpreter.html.
    
    $ python wget.py http://docs.python.org/tutorial/
    saving http://docs.python.org/tutorial/ as index.html.

> You can find the solution [here](problem_05.py).

### Problem 6
Write a program `antihtml.py` that takes a URL as argument, downloads the html from 
web and print it after stripping html tags using regex.

    $ python antihtml.py index.html
    ...
    The Python interpreter is usually installed as /usr/local/bin/python on
    those machines where it is available; putting /usr/local/bin in your
    ...

> You can find the solution [here](problem_06.py).

### Problem 7
Write a function make_slug that takes a name converts it into a slug. 
A slug is a string where spaces and special characters are replaced by a hyphen, 
typically used to create blog post URL from post title. It should also make sure 
there are no more than one hyphen in any place and there are no hyphens at the 
biginning and end of the slug.

    >>> make_slug("hello world")
    'hello-world'
    >>> make_slug("hello  world!")
    'hello-world'
    >>> make_slug(" --hello-  world--")
    'hello-world'

> You can find the solution [here](problem_07.py).

### Problem 8
Write a program links.py that takes URL of a webpage as argument and prints 
all the URLs linked from that webpage.

> You can find the solution [here](problem_08.py).

### Problem 9
Write a regular expression to validate a phone number.

> You can find the solution [here](problem_09.py).
