class Extend():
    def example1(self):
        seq = [1, 2, 3, 4]
        a, b, c, d, = seq
        print("Example1\n")
        print(a, b, c, d)

        a, *b = seq
        print("\n")
        print(a)
        print(b)

        *a, b = seq
        print("\n")
        print(a)
        print(b)

        a, *b, c = seq
        print("\n")
        print(a)
        print(b)
        print(c)

        a, b, *c = seq
        print("\n")
        print(a)
        print(b)
        print(c)

    def example2(self):
        a, *b = "spam"
        print("Example2\n")
        print(a, b)

        a, *b, c = "spam"
        print("\n")
        print(a, b, c)

        a, *b, c = range(4)
        print("\n")
        print(a, b, c)

    def example3(self):
        S = "spam"
        print("Example3\n")
        print(S[0], S[1:])      # Slices are type-specific, *assignment always return a list
        print("\n")
        print(S[0], S[1:3], S[3])

    def example4(self):
        L = [1, 2, 3, 4]
        print("Example4\n")
        while L:
            front, *L = L       # Get first, rest without slicing
            print(front, L)
