class GlobalStatement():
    X = 88                  # Global X
    def example1(self):
        print("Example1\n")             
        def func():
            global X
            X = 99          # Global X: outside def

        func()
        print(X)            # Prints 99

    def example2(self):
        y, z = 1, 2         # Global variables in module
        print("Example2\n")
        def all_global():
            global x        # Declare globals assigned
            x = y + z       # No need to declare y, z: LEGB rule
         
        all_global()
        print(x)

    # Program design: Minimize Global Variables
    X = 99
    def example3(self):
        print("Example3\n")
        def func1():
            global X
            X = 88

        def func2():
            global X
            X = 77

        func1()
        print(X)
        func2()
        print(X)

    # Program design: Minimize Global Variables
    def example4(self):
        print("Example4\n")
        import first
        print(first.X)      # OK: references a name in another file
        first.X = 88        # Bur changing it can be too subtle and implicit
        print(first.X)

    # Program design: Minimize Global Variables
    def example5(self):
        print("Example5\n")
        import first
        first.setX(88)      # Call the function instead of changing directly
        print(first.X)

    # Other ways to access globals
    def example6(self):
        print("Example6\n")
        import thismod
        thismod.test()
        print(thismod.var)




        
             