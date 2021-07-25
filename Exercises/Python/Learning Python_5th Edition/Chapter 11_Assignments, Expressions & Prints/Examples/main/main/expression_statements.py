class Expression():
    # Expression statements
    def example1(self):
        x = print("spam")       # print is a function call expression in 3.X
        print("Example1\n")
        print(x)                # But it is coded as an expression statement

    # Append is an in-place change
    def example2(self):
        L = [1, 2]
        L.append(3)
        print("Example2\n")
        print(L)

        L = L.append(4)         # But append returns None, not L
        print("\n")
        print(L)                # So we lose our list!