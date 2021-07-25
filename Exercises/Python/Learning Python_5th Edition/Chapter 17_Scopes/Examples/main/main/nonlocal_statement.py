class NonLocal():
    # nonlocal in Action
    def example1(self):
        print("Example1\n")
        def tester(start):
            state = start               # Referencing non local works normally
            def nested(label):
                print(label, state)     # Remembers state in enclosing scope
            return nested

        F = tester(0)
        print(F("spam"))
        print(F("ham"))

    # nonlocal in Action
    def example2(self):
        print("Example2\n")
        def tester(start):
            state = start               
            def nested(label):
                print(label, state)     
                #state += 1              # Cannot change by default (never in 2.X)
            return nested

        F = tester(0)
        print(F("spam"))

    # Using nonlocal for changes
    def example3(self):
        print("Example3\n")
        def tester(start):
            state = start               # Each call gets its own state
            def nested(label):
                nonlocal state          # Remembers state in enclosing scope
                print(label, state)     
                state += 1              # Allowed to change it if nonlocal
            return nested

        F = tester(0)
        print(F("spam"))                # Increments state on each call
        print(F("ham")) 
        print(F("eggs")) 

        G = tester(42)                  # Make a new tester that starts at 42
        print(G("spam"))                # My state information updated at 43
        print(G("eggs"))                # But F's is where it left off: at 3
        print(F("bacon"))               # Each call has different state information

    # Boundary cases
    def example4(self):
        print("Example4\n")
        def tester(start):
            def nested(label):
                #nonlocal state          # Nonlocals must already exist in enclocing def!
                state = 0
                print(label, state)
            return nested

    # Boundary cases
    def example5(self):
        print("Example5\n")
        def tester(start):
            def nested(label):
                global state            # Globals don't have to exist yet when declared
                state = 0
                print(label, state)     # This creates the name in the module now
            return nested

        F = tester(0)
        print(F("abc"))
        print(state)

    # Boundary cases
    spam = 99
    def example6(self):
        print("Example6\n")
        #def tester():
            #def nested():
                #nonlocal spam           # Must be in a def, not the module!
                #print("Current=", spam)
                #spam += 1
            #return nested

        #F = tester()
        #print(F())
        #print(F())


