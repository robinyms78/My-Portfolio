class Functions():
    # A First Example: Definitions and Calls
    def example1(self):
        def times(x, y):       # Create and assign function
            return x * y       # Body executed when called

        print(times(2, 4))     # Arguments in parenthesis
        x = times(3.14, 4)     # Save the result object
        print(x)
        print(times("Ni", 4))  # Functions are "typeless" 

    # A Second Example: Intersecting Sequences
    def example2(self):
        def intersect(seq1, seq2):
            res = []                # Start empty
            for x in seq1:          # Scan seq1    
                if x in seq2:       # Common item?
                    res.append(x)   # Add to end
            return res

        s1 = "SPAM"
        s2 = "SCAM"
        print(intersect(s1, s2))    # Strings

    # A Second Example: Intersecting Sequences
    def example3(self):
        s1 = "SPAM"
        s2 = "SCAM"
        print([x for x in s1 if x in s2])

    # Polymorphism Revisited
    def example4(self):
        def intersect(seq1, seq2):
            res = []                # Start empty
            for x in seq1:          # Scan seq1    
                if x in seq2:       # Common item?
                    res.append(x)   # Add to end
            return res

        x = intersect([1,2,3], (1,4))   # Mixed types
        print(x)                        # Saved result object

