import os

class Iterations():
    def example1(self):
        for x in [1, 2, 3, 4]:          # In 2.X: print x ** 2
            print(x ** 2, end = " ")

        print("\n")
        for x in (1, 2, 3, 4):
            print(x ** 3, end = " ")

        print("\n")
        for x in "spam":
            print(x * 2, end = " ")
           
    # The Iteration Protocol: File Iterators:
    def example2(self):
        print("\n")
        print(open("script2.py").read())
        open("script2.py").read()

    # The Iteration Protocol: File Iterators
    def example3(self):
        print("\n")
        f = open("script2.py")      # Read a four-line script file in this directory
        print(f.readline())
        print(f.readline())
        print(f.readline())
        print(f.readline())         # Last lines may have a \n or not 
        print(f.readline())         # Return empty string at end of file

    # The Iteration Protocol: File Iterators
    def example4(self):
        print("\n")
        f = open("script2.py")      # __next__ loads one line on each call too
        print(f.__next__())         # But raises an exception at end-of-file
        print(f.__next__())         # Use f.next() in 2.X, or next(f) in 2.X or 3.X
        print(f.__next__()) 
        print(f.__next__()) 
        #print(f.__next__()) 

    # The Iteration Protocol: File Iterators
    def example5(self):
        print("\n")
        for line in open("script2.py"):         # Use file iterators to read by lines
            print(line.upper(), end = "")       # Calls __next__, catches StopIteration

    # The Iteration Protocol: File Iterators
    def example6(self):
        print("\n")
        for line in open("script2.py").readlines():
            print(line.upper(), end = "")

    # The Iteration Protocol: File Iterators
    def example7(self):
        print("\n")
        f = open("script2.py")
        while True:
            line = f.readline()
            if not line:
                break
            print(line.upper(), end = "")

    # Manual Iteration: iter and next
    def example8(self):
        print("\n")
        f = open("script2.py")
        print(f.__next__())         # Call iteration method directly
        print(f.__next__())

    # Manual Iteration: iter and next
    def example9(self):
        print("\n")
        f = open("script2.py")
        print(next(f))              # The next(f) built-in calls f.__next__() in 3.X
        print(next(f))              # next(f) -> [3.X: f.__next__()], [2.X: f.next()]


    # The full iteration protocol
    def example10(self):
        L = [1, 2, 3]
        I = iter(L)                 # Obtain an iterator object from an iterable
        print(I.__next__())         # Call iterator's next to advance to next item
        print(I.__next__())         # Or use I.next() in 2.X, next(I) in either line
        print(I.__next__())
        #print(I.__next__())

    # The full iteration protocol
    def example11(self):
        print("\n")
        f = open("script2.py")
        print(iter(f) is f)
        print(iter(f) is f.__iter__())
        print(f.__next__())

    # The full iteration protocol
    def example12(self):
        print("\n")
        L = [1, 2, 3]
        print(iter(L) is L)
        #print(L.__next__())
        I = iter(L)
        print(I.__next__())
        print(next(I))              # Same as I.__next__()

    # Manual iteration
    def example13(self):
        print("\n")
        L = [1, 2, 3]
        for X in L:                     # Automatic iteration
            print(X ** 2, end = " ")    # Obtains iter, calls __next__, catches exception    

    # Manual iteration
    def example14(self):
        print("\n")
        L = [1, 2, 3]
        I = iter(L)
        while True:                     # Manual iteration: what for loops usually do
            try:                        # try statement catches exception
                X = next(I)             # Or call I.__next__() in 3.X
            except StopIteration:
                break
            print(X ** 2, end = " ")

    # Other Built-in Type Iterables
    def example15(self):
        print("\n")
        D = {"a": 1, "b": 2, "c": 3}
        for key in D.keys():
            print(key, D[key])
        I = iter(D)
        print(next(I))
        print(next(I))
        print(next(I))
        #print(next(I))

    # Other Built-in Type Iterables
    def example16(self):
        print("\n")
        D = {"a": 1, "b": 2, "c": 3}
        for key in D:
            print(key, D[key])

    # Other Built-in Type Iterables
    def example17(self):
        print("\n")
        P = os.popen("dir")
        print(P.__next__())
        print(P.__next__())
        #print(next(P))

    # Other Built-in Type Iterables
    def example18(self):
        print("\n")
        P = os.popen("dir")
        I = iter(P)
        print(next(I))
        print(I.__next__())

    # Other Built-in Type Iterables
    def example19(self):
        print("\n")
        R = range(5)
        print(R)            # Ranges are iterables in 3.X
        I = iter(R)         # Use iteration protocol to produce results
        print(next(I))
        print(next(I))
        print(list(range(5)))   # Or use list to collect all results at once

    # Other Built-in Type Iterables
    def example20(self):
        print("\n")
        E = enumerate("spam")
        print(E)                # enumerate is an iterable too
        I = iter(E)             
        print(next(I))          # Generate results with iteration protocol
        print(next(I))
        print(list(enumerate("spam")))  # Or use list to force generation to run










