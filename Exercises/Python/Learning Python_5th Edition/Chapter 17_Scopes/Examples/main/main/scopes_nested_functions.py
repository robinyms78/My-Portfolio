class Nested():
    # Nested Scope Examples
    def example1(self):
        print("Example1\n")
        X = 99              # Global scope name: not used
        def f1():       
            X = 88          # Enclosing def local
            def f2():
                print(X)    # Reference made in nested def

            f2()
        f1()                # Prints 88: enclosing def local

    # Nested Scope Examples
    def example2(self):
        print("Example2\n")
        def f1():
            X = 88
            def f2():
                print(X)    # Remembers X in enclosing def scope
            return f2       # Returns f2 but doesn't call it

        action = f1()       # Make, return function
        action()            # Call it now, prints 88

    # A simple function factory
    def example3(self):
        print("Example3\n")
        def maker(N):
            def action(X):  # Make and return action
                return X ** N
            return action   # action retains N from enclosing scope

        f = maker(2)        # Pass 2 to argument N
        print(f)
        print(f(3))         # Pass 3 to X, N remembers 2: 3 ** 2
        print(f(4))         # 4 ** 2

        g = maker(3)        # g remembers 3, f remembers 2
        print(g(4))         # 4 ** 3
        print(f(4))         # 4 ** 2

    # A simple function factory
    def example4(self):
        print("Example4\n")
        def maker(N):
            return lambda X: X ** N     # lambda functions retain state too

        h = maker(3)                    # 4 ** 3 again
        print(h(4))

    # Retaining Enclosing Scope State with defaults
    def example5(self):
        print("Example5\n")
        def f1():
            x = 88
            def f2(x = x):      # Remember enclosing scope X with defaults
                print(x)
            f2()
        f1()                    # Prints 88

    # Retaining Enclosing Scope State with defaults
    def example6(self):
        print("Example6\n")
        def f1():
            x = 88              # Pass x along instead of nesting
            f2(x)               # Forward reference OK

        def f2(x):              # Flat is still often better than nested!
            print(x)

        f1()

    # Nested scopes, defaults, and lambdas
    def example7(self):
        print("Example7\n")
        def func():
            x = 4
            action = (lambda n: x ** n)
            return action           # x remebered from enclosing def

        x = func()
        print(x(2))

    # Nested scopes, defaults, and lambdas
    def example8(self):
        print("Example8\n")
        def func():
            x = 4
            action = (lambda n, x = x: x ** n)
            return action           # Pass x in manually

        x = func()
        print(x(2))

    # Loop variables may require default, not scopes
    def example9(self):
        print("Example9\n")
        def makeActions():
            acts = []
            for i in range(5):                  # Tries to remember each i
                acts.append(lambda x: i ** x)   # But all remember same last i!
            return acts

        acts = makeActions()
        print(acts[0])
        print(acts[0](2))           # All are 4 ** 2, 4 = value of last i
        print(acts[1](2))           # This should be 1 ** 2(1)
        print(acts[2](2))           # This should be 2 ** 2(4)
        print(acts[4](2))           # Only this should be 4 ** 2(16)
        
    # Loop variables may require defaults, not scope
    def example10(self):
        print("Example10\n")
        def makeActions():
            acts = []
            for i in range(5):                          # Use defaults instead
                acts.append(lambda x, i = i: i ** x)    # Remember current i
            return acts

        acts = makeActions()
        print(acts[0](2))                  # 0 ** 2
        print(acts[1](2))                  # 1 ** 2
        print(acts[2](2))                  # 2 ** 2
        print(acts[4](2))                  # 4 ** 2

    # Arbitrary scope nesting
    def example11(self):
        print("Example11\n")
        def f1():
            x = 99
            def f2():
                def f3():
                    print(x)        # Found in f1's local scope!
                f3()
            f2()
        f1()








    

















     




        
        
           



        
        
         
    








