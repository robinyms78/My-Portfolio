class Useful():
    def example1(self):
        seq = [1, 2, 3, 4]
        a, *b = seq     # First, rest
        print("Example1\n")
        print(a, b)

        a, b = seq[0], seq[1:]      # First, rest: traditional
        print("\n")
        print(a, b)

        *a, b = seq                 # Rest, last
        print("\n")
        print(a, b)

        a, b = seq[:-1], seq[-1]    # Rest, last: traditional
        print("\n")
        print(a, b)




