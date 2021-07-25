class For():
    # Basic usage
    def example1(self):
        for x in ["spam", "eggs", "ham"]:
            print(x, end = " ")

    # Basic usage
    def example2(self):
        sum = 0
        print("\n")
        for x in [1, 2, 3, 4]:
            sum = sum + x
        print(sum)

    # Basic usage
    def example3(self):
        prod = 1
        for item in [1, 2, 3, 4]:
            prod *= item
        print(prod)

    # Other data types
    def example4(self):
        S = "lumberjack"
        T = ("and", "I'm", "okay")
        for x in S:                 # Iterate over a string
            print(x, end = " ")

        for x in T:                 # Iterate over a tuple
            print(x, end = " ")

    # Tuple assignment in for loops
    def example5(self):
        print("\n")
        T = [(1, 2), (3, 4), (5, 6)]
        for (a, b) in T:            # Tuple assignment at work
            print(a, b)

    # Tuple assignment in for loops
    def example6(self):
        print("\n")
        D = {"a": 1, "b": 2, "c": 3}
        for key in D:                   # Use dict keys iterator and index
            print(key, "=>", D[key])

    # Tuple assignment in for loops
    def example7(self):
        D = {"a": 1, "b": 2, "c": 3}
        print(list(D.items()))
        for (key, value) in D.items():  # Iterate over both keys and values
            print(key, "=>", value)

    # Tuple assignment in for loops
    def example8(self):
        D = {"a": 1, "b": 2, "c": 3}
        for both in D.items():
            a, b = both                 # Manual assignment equivalent
            print(a, b)                 # 2.X: prints with enclosing tuple "()"

    # Tuple assignment in for loops
    def example9(self):
        ((a, b), c) = ((1, 2), 3)       # Nested sequences work too
        print(a, b, c)

    # Tuple assignment in for loops
    def example10(self):
        for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]:
            print(a, b, c)

    # Tuple assignment in for loops
    def example11(self):
        for ((a, b), c) in [([1, 2], 3), ["XY", 6]]:
            print(a, b, c)

    # Python 3.X extended sequence assignment
    def example12(self):
        a, b, c = (1, 2, 3)         # Tuple assignment
        print(a, b, c)

        for (a, b, c) in [(1, 2, 3), (4, 5, 6)]:
            print(a, b, c)          # Used in for loop

    # Python 3.X extended sequence assignment in for loops
    def example13(self):
        a, *b, c = (1, 2, 3, 4)     # Extended seq assignment
        print(a, b, c)
        for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
            print(a, b, c)

    # Python 3.X extended sequence assignment in for loops
    def example14(self):
        for all in [(1, 2, 3, 4), (5, 6, 7, 8)]:        # Manual slicing in 2.X
            a, b, c = all[0], all[1:3], all[3]
            print(a, b, c)

    # Nested for loops
    def example15(self):
        items = ["aaa", 111, (4, 5), 2.01]      # A set of objects
        tests = [(4, 5), 3.14]                  # Keys to search for

        for key in tests:           # For all keys
            for item in items:      # For all items
                if item == key:
                    print(key, "was found")
                    break
            else:
                print(key, "not found!")

    # Nested for loops
    def example16(self):
        items = ["aaa", 111, (4, 5), 2.01]      # A set of objects
        tests = [(4, 5), 3.14]                  # Keys to search for

        for key in tests:                       # For all keys
            if key in items:                    # Let Python check for a match
                print(key, "was found")
            else:
                print(key, "not found")

    # Nested for loops
    def example17(self):
        seq1 = "spam"
        seq2 = "scam"

        res = []                                # Start empty
        for x in seq1:                          # Scan first sequence
            if x in seq2:                       # Common item?
                res.append(x)                   # Add to result end
        print(res)

    # Nested for loops
    def example18(self):
        seq1 = "spam"
        seq2 = "scam"

        print([x for x in seq1 if x in seq2])          # Let Python collect results












             







