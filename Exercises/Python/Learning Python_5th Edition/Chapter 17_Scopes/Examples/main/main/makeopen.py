class MakeOpen():
    def example1(self):
        import builtins
        def makeopen(id):
            original = builtins.open
            def custom(*pargs, **kargs):
                print("Custom open call %r:" %id, pargs, kargs)
                return original(*pargs, **kargs)
            builtins.open = custom

        print("Example1\n")
        F = open("script2.py")                      # Call built-in open in builtins
        print(F.read())

        from makeopen import MakeOpen               # Import open resetter function
        makeopen("spam")                            # Custom open calls built-in open

        F = open("script2.py")                      # Call custom open in builtins
        print(F.read())

        makeopen("eggs")                            # Nested customizers work too!
        F = open("script2.py")                      # Because each retains own state
        print(F.read())

    def example2(self):
        import builtins
        class makeopen:                             # See Part VI: Call catches self()
            def __init__(self, id):
                self.id = id
                self.original = builtins.open
                builtins.open = self

            def __call__(self, *pargs, **kargs):
                print("Custom open call %r:" %self.id, pargs, kargs)
                return self.original(*pargs, **kargs)

        print("Example2\n")
        F = open("script2.py")                      # Call built-in open in builtins
        print(F.read())

        from makeopen import MakeOpen               # Import open resetter function
        makeopen("spam")                            # Custom open calls built-in open

        F = open("script2.py")                      # Call custom open in builtins
        print(F.read())

        makeopen("eggs")                            # Nested customizers work too!
        F = open("script2.py")                      # Because each retains own state
        print(F.read())



