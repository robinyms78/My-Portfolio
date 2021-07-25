class State():
    # State with nonlocal: 3.X only
    def example1(self):
        print("Example1\n")
        def tester(start):
            state = start               # Each call gets its own state
            def nested(label):
                nonlocal state          # Remembers state in enclosing state
                print(label, state)     
                state += 1              # Allowed to change it if nonlocal
            return nested

        F = tester(0)
        print(F("spam"))                # State visible within closure only
        #print(F.state)

    # State with Globals: A Single Copy Only
    def example2(self):
        print("Example2\n")
        def tester(start):
            global state                # Move it out to the module to change it
            state = start
            def nested(label):          # global allows changes in module scope
                global state            
                print(label, state)
                state += 1
            return nested

        F = tester(0)
        print(F("spam"))                # Each call increments shared global state
        print(F("eggs"))
        G = tester(42)                  # Resets state's single copy in global scope
        print(G("toast"))
        print(G("bacon"))
        print(F("ham"))                 # But my counter has been overwitten

    # State with Classes: Explicit Attributes (Preview)
    def example3(self):
        class tester:                       # Class-based alternative (See Part VI)
            def __init__(self, start):
                self.state = start          # Save state explicitly in new object

            def nested(self,label):
                print(label, self.state)    # Reference state explicitly
                self.state += 1
        
        print("Example3\n")
        F = tester(0)                   # Create instance, invoke __init__
        print(F.nested("spam"))         # F is passed to self
        print(F.nested("ham"))          # Each instance gets new copy of state
        G = tester(42)                  # Changing one does not impact others
        print(G.nested("toast"))               
        print(G.nested("bacon"))
        print(F.nested("eggs"))         # F's state is where it left off
        print(F.state)                  # State may be accessed outside class

    # State with Classes: Explicit Attributes (Preview)
    def example4(self):
        class tester:
            def __init__(self, start):
                self.state = start

            def __call__(self, label):      # Intercept direct instance calls
                print(label, self.state)    
                self.state += 1             # So .nested() not required

        print("Example4\n")
        H = tester(99)
        print(H("juice"))                   # Invokes __call__
        print(H("pancakes"))

    # State with Function Attributes: 3.X and 2.X
    def example5(self):
        def tester(start):
            def nested(label):
                print(label, nested.state)     # nested is in enclosing scope
                nested.state += 1              # Change attr, but nested itself
            nested.state = start               # Initial state after func defined
            return nested

        print("Example5\n")
        F = tester(0)
        print(F("spam"))                       # F is a "nested" with state attached
        print(F("ham"))                 
        print(F.state)                         # Can access state outside functions too

        G = tester(42)                         # G has own state, and don't overwrite F's
        print(G("eggs"))
        print(F("ham"))
        print(F.state)                         # State is accessible and per-call 
        print(G.state)
        print(F is G)                          # Different function objects

    # State with Mutables: Obscure ghost at Python's past?
    def example6(self):
        def tester(start):
            def nested(label):
                print(label, state[0])      # Leverage in-place mutable change
                state[0] += 1
            state = [start]                 # Extra syntax, deep magic?
            return nested

        print("Example6\n")
        F = tester(0)
        print(F("spam"))                       # F is a "nested" with state attached
        print(F("ham"))                 

        G = tester(42)                         # G has own state, and don't overwrite F's
        print(G("eggs"))
        print(F("ham"))








