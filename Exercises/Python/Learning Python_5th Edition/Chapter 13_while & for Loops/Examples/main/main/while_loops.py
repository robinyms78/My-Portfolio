class While():
    def example1(self):
        while True:
            print("Type Crlt-C to stop me!")

    def example2(self):
        x = "spam"
        while x:                    # While x is not empty
            print(x, end = " ")     # In 2.x use print x, 
            x = x[1:]               # strip first character off x

    def example3(self):
        a = 0; b = 10
        print("\n")
        while a < b:                # One way to code counter loops
            print(a, end = " ")
            a += 1                  # Or, a = a + 1
