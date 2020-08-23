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

### Problem 10
Write a program `myip.py` to print the external IP address of the machine. 
Use the response from `http://httpbin.org/get` and read the IP address from there. 
The program should print only the IP address and nothing else.

> You can find the solution [here](problem_10.py).

### Problem 11
Write a python program `zip.py` to create a zip file. 
The program should take name of zip file as first argument and files 
to add as rest of the arguments.

    $ python zip.py foo.zip file1.txt file2.txt

> You can find the solution [here](problem_11.py)

### Problem 12
Write a program `mydoc.py` to implement the functionality of `pydoc`. 
The program should take the module name as argument and print documentation 
for the module and each of the functions defined in that module.

    $ python mydoc.py os
    Help on module os:
    
    DESCRIPTION
    
    os - OS routines for Mac, NT, or Posix depending on what system we're on.
    ...
    
    FUNCTIONS
    
    getcwd()
        ...

Hints:
* The `dir` function to get all entries of a module
* The `inspect.isfunction` function can be used to test if given object is a function
* `x.__doc__` gives the docstring for x.
* The `__import__` function can be used to import a module by name

> You can find the solution [here](problem_12.py)

### Problem 13
Write a program `csv2xls.py` that reads a csv file and exports it as Excel file. 
The program should take two arguments. The name of the csv file to read as 
first argument and the name of the Excel file to write as the second argument.

> You can find the solution [here](problem_13.py)

### Problem 14
Create a new virtualenv and install BeautifulSoup. 
BeautifulSoup is very good library for parsing HTML. 
Try using it to extract all HTML links from a webpage.

> You can find the solution [here](problem_14.py)
