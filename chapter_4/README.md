## 4. Object Oriented Programming

### Problem 1
What will the output of the following program.

    class A:
        def f(self):
            return self.g()
    
        def g(self):
            return 'A'
    
    class B(A):
        def g(self):
            return 'B'
    
    a = A()
    b = B()
    print(a.f(), b.f())
    print(a.g(), b.g())

> You can find the solution [here](problem_01.py).

### Problem 2
What will be the output of the following program?

    try:
        print "a"
    except:
        print "b"
    else:
        print "c"
    finally:
        print "d"

> You can find the solution [here](problem_02.py).

### Problem 3
What will be the output of the following program?

    try:
        print("a")
        raise Exception("doom")
    except:
        print("b")
    else:
        print("c")
    finally:
        print("d")

> You can find the solution [here](problem_03.py).

### Problem 4
What will be the output of the following program?

    def f():
        try:
            print("a")
            return
        except:
            print("b")
        else:
            print("c")
        finally:
            print("d")
    
    f()

> You can find the solution [here](problem_04.py).
