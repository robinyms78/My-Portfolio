class Sequence():
    def example1(self):
        # Basic assignment
        nudge = 1
        wink= 2
        
        # Tuple assignment
        A, B = nudge, wink      # Like A = nudge, B = wink
        print("Example1\n")
        print(A,B)

        #List assignment
        [C, D] = [nudge, wink]
        print(C,D)

    def example2(self):
        nudge = 1
        wink = 2
        nudge, wink = wink, nudge             # Tuples: swaps values
        print("Example2\n")
        print(nudge, wink)                    # Like T = nudge; nudge = wink; wink = T

    def example3(self):
        [a, b, c] = (1, 2, 3)       # Assign tuple of values to list of names
        print("Example3\n")
        print(a, c)

        (a, b, c) = "ABC"           # Assign string of characters to tuple
        print(a, c)

