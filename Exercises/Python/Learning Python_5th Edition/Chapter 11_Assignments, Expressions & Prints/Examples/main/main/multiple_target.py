class Multiple():
    def example1(self):
        # Multiple-target assignment
        a = b = c = "spam"
        print("Example1\n")
        print(a, b, c)

        c = "spam"
        b = c
        a = b
        print("\n")
        print(a, b, c)

    # Multiple-target assignment and shared references
    def example2(self):
        a = b = 0
        b = b + 1
        print("Example2\n")
        print(a, b)

    # Multiple-target assignment and shared references
    def example3(self):
        a = b = []
        b.append(42)
        print("\n")
        print(a, b)

    # Multiple-target assignment and shared references
    def example4(self):
        a = []          # a, and b do not share the same object
        b = []
        b.append(42)
        print("\n")
        print(a, b)

        a, b = [], []   # a, and b do not share the same object
        b.append(42)
        print("\n")
        print(a, b)