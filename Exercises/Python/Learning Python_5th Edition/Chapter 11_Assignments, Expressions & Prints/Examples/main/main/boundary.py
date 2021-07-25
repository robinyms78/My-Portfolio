class Boundary():
    def example1(self):
        seq = [1, 2, 3, 4]
        a, b, c, *d = seq
        print("Example1\n")
        print(a, b, c, d)

        a, b, c, d, *e = seq
        print("\n")
        print(a, b, c, d, e)

        a, b, *e, c, d = seq
        print("\n")
        print(a, b, c, d, e)

    def example2(self):
        seq = [1, 2, 3, 4]
        print("Example2\n")
        #a, *b, c, *d = seq     # Syntax error

        #a, b = seq              # Value error
        #print(a, b)
        
        #*a = seq                # Syntax error
        #print(a)

        *a, = seq
        print(a)