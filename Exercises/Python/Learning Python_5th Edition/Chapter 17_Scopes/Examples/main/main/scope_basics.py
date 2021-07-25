class ScopeBasic():
    def example1(self):
        print("Example1\n")
        X = 99          # Global (module) scope X
        def func():     # local (function) scope X: a different variable
            X = 88

        print(X)
        func()
        print(X)

    # Scope example
    def example2(self):
         # Global scope
         print("Example2\n")
         X = 99                 # X and func assigned in module: global

         def func(Y):           # Y and Z  assigned in function: locals
             # local scope
             Z = X + Y          # X is a global
             return Z

         print(func(1))         # func in module: results = 100

    # The Built-in Scope
    def example3(self):
        import builtins
        print("Example3\n")
        print(dir(builtins))
        print(zip)              # The normal way

    # The Built-in Scope
    def example4(self):
        import builtins             # The hard way: for customizations
        print("Example4\n")
        print(builtins.zip)
        print(zip is builtins.zip)  # Same object, different lookups

    # Redefining built-in names: For better or worse
    def example5(self):
        def hider():
            print("Example5\n")
            open = "spam"           # Local variable, hides built-in here
            #open("data.txt")        # Error: this no longer opens a file in this scope!    

        hider()

    # Redefining built-in names: For better or worse
    def example6(self):
        print("Example6\n")
        import builtins
        open = 99                   # Assign in global scope, hides built-in here too
        print(len(dir(builtins)), len([x for x in dir(builtins) if not x.startswith("__")]))

    # Redefining built-in names: For better or worse
    def example7(self):
        X = 88                      # Global X
        def func():                 # Local X: hides global, but we want this here
            X = 99
            
        print("Example7\n")
        func()
        print(X)                    # Prints 88: unchanged
