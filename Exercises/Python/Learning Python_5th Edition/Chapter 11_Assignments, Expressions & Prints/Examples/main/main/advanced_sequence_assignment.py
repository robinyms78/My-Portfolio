class Advance():
    def example1(self):
        string = "SPAM"
        a, b, c, d = string     # Same number on both sides
        print("Example1\n")
        print(a, d)

        #a, b, c, = string       # Error if not

    def example2(self):
        string = "SPAM"
        a, b, c = string[0], string[1], string[2:]      # Index and slice
        print("Example2\n")
        print(a, b, c)

        a, b, c = list(string[:2]) + [string[2:]]       # Slice and concatenate
        print(a, b, c)

        a, b = string[:2]   # Same, but simpler
        c = string[2:]
        print(a, b, c)

        (a, b), c = string[:2], string[2:]  # Nested sequence
        print(a, b, c)

        ((a, b), c) = ("SP", "AM")          # Paired by shape and position
        print(a, b, c)

    def example3(self):
        red, green, blue = range(3)
        print("Example3\n")
        print(red, blue)

        print(list(range(3)))   # list() required in Python 3.X only

        L = [1, 2, 3, 4]        # See next section for 3.X *alternative
        while L:
            front, L = L[0], L[1:]
            print(front, L)




