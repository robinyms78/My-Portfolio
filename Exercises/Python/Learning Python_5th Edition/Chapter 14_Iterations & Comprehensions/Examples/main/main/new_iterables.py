class Iterables():
    # Impacts on 2.X Code: Pros and Cons
    def example1(self):
        print("\n")
        print(zip("abc", "xyz"))             # An iterable in Python 3.X (a list in 2.X)
        print(list(zip("abc", "xyz")))       # Force list of results in 3.X to display
        Z = zip((1, 2), (3, 4))              # Unlike 2.X lists, cannot index, etc
        #print(Z[0]) 

    # Impacts on 2.X Code: Pros and Cons
    def example2(self):
        print("\n")
        M = map(lambda x: 2 ** x, range(3))
        for i in M:
            print(i)
        for i in M:         # Unlike 2.X lists, one pass only (zip too)
            print(i)

    # The range iterable
    def example3(self):
        print("\n")
        R = range(10)            # range returns on iterable, not a list
        print(R)
        I = iter(R)              # Make an iterator fro the range iterable
        print(next(I))           # Advance to next result
        print(next(I))           # What happens in for loops, comprehensions, etc
        print(next(I))
        print(list(range(10)))   # To force a list if required

    # The range iterable
    def example4(self):
        print("\n")
        R = range(10) 
        print(len(R))           # range also does len and indexing, but not others
        print(R[0])
        print(R[-1])
        #print(next(I))          # Continue taking from iterator, where left off
        #print(I.__next__())     # next() becomes __next__(), but uses new next()

    # The map, zip, and filter iterables
    def example5(self):
        print("\n")
        M = map(abs, (-1, 0, 1))        # map returns an iterable, not a list
        print(M)
        print(next(M))                  # Use iterator manually: exhausts results
        print(next(M))                  # These do not support len() or indexing
        print(next(M))
        #print(next(M))
        for x in M:                     # map iterator is now empty: one pass only
            print(x)

    # The map, zip, and filter iterables
    def example6(self):
        print("\n")
        M = map(abs, (-1, 0, 1))            # Make a new iterable/iterator to scan again
        for x in M:                         # Iteration contexts auto call next()
            print(x)
        print(list(map(abs, (-1, 0, 1))))   # Can force a real list if needed

    # The map, zip, and filter iterables
    def example7(self):
        print("\n")
        Z = zip((1,2,3), (10, 20, 30))      # zip is the same: a one-pass iterator
        print(Z)
        print(list(Z))
        for pair in Z:                      # Exhausted after one pass
            print(pair)

    # The map, zip, and filter iterables
    def example8(self):
        print("\n")
        Z = zip((1,2,3), (10,20,30))
        for pair in Z:                      # Iterator used automatically or manually
            print(pair)

    # The map, zip, and filter iterables
    def example9(self):
        print("\n")
        Z = zip((1,2,3), (10,20,30))        # Manual iteration (iter() not needed)
        print(next(Z))
        print(next(Z))

    # The map, zip, and filter iterables
    def example10(self):
        print("\n")
        print(filter(bool, ["spam", "", "ni"]))
        print(list(filter(bool, ["spam", "", "ni"])))

    # The map, zip, and filter iterables
    def example11(self):
        print("\n")
        print([x for x in ["spam", "", "ni"] if bool(x)])
        print([x for x in ["spam", "", "ni"] if x])

    # Multiple vs single pass iterators
    def example12(self):
        print("\n")
        R = range(3)        # range allows multiple iterators
        #print(next(R))
        I1 = iter(R)
        print(next(I1))
        print(next(I1))
        I2 = iter(R)        # Two iterables on on range
        print(next(I2))
        print(next(I1))     # I1 is at different spot than I2

    # Multiple vs single pass iterators
    def example13(self):
        print("\n")
        Z = zip((1, 2, 3), (10, 11, 12))
        I1 = iter(Z)
        I2 = iter(Z)        # Two iterators on one zip
        print(next(I1))
        print(next(I1))
        print(next(I2))

    # Multiple vs single pass iterators
    def example14(self):
        print("\n")
        M = map(abs, (-1, 0, 1))    # Ditto for map (and filter)
        I1 = iter(M)
        I2 = iter(M)
        print(next(I1), next(I2), next(I1))
        #print(next(I2))             # (3.X) single scan is exhausted"

    # Multiple vs single pass iterators
    def example15(self):
        print("\n")
        R = range(3)                # But range allows many iterators
        I1, I2 = iter(R), iter(R)
        print([next(I1), next(I1), next(I1)])
        print(next(I2))             # Multiple active scans, like 2.X lists
            
    # Dictionary view iterables
    def example16(self):
        print("\n")
        D = dict(a=1, b=2, c=3)
        print(D)
        K = D.keys()                # A view object in 3.X. not a list
        print(K)
        #print(next(K))             # Views are not iterables themselves
        I = iter(K)                 # View iterables have an iterator
        print(next(I))              # which can be used manually
        print(next(I))              # but does not support len(), index
        for k in D.keys():          # All iteration contexts use auto
            print(k, end = " ")

    # Dictionary view iterables
    def example17(self):
        print("\n")
        D = dict(a=1, b=2, c=3)
        K = D.keys()
        print(list(K))              # Can still force a real list if needed
        V = D.values()
        print(V)                    # Ditto for values() and items() view
        #print(V[0])                # Need list() to display or index as list
        print(list(V)[0])
        print(list(D.items()))
        for (k,v) in D.items():
            print(k, v, end = " ")

    # Dictionary view iterables
    def example18(self):
        print("\n")
        D = dict(a=1, b=2, c=3)     
        print(D)                    # Dictionaries still produce an iterator
        I = iter(D)                 
        print(next(I))              # Returns next key on each iteration
        print(next(I))
        for key in D:               # Still no need to call keys() to iterate
            print(key, end = " ")   # But keys is an iterable in 3.X too!

    # Dictionary view iterables
    def example19(self):
        print("\n")
        D = dict(a=1, b=2, c=3)     
        print(D)  
        for k in sorted(D.keys()):
            print(k, D[k], end = " ")
        print("\n")
        for k in sorted(D):             # "Best practice" key sorting
            print(k, D[k], end = " ")