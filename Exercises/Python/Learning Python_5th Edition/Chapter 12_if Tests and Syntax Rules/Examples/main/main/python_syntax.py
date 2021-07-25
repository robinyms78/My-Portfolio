class Python_Syntax():
    # Block delimiters: Indentation rules
    def example1(self):
        x = 1
        if x:
            y = 2
            if y:
                print("block2")
            print("block1")
        print("block0")

    # Block delimiters: Indentation rules
    def example3(self):
        x = "SPAM"                      # Error: first line indented
        if "rubbery" in "shrubbery":
            print(x*8)                  # Prints 8 "SPAM"
            x += "NI"
            if x.endswith("NI"):
                x *= 2
                print(x)                # Prints "SPAMNISPAMNI" 

    # A few special case
    def example4(self):
        L = ["Good",   # Open pairs may span lines
             "Bad",
            "Ugly"]   

    # A few special case
    def example5(self):
        if a == b and c == d and \
            d == e and f == g:
            print("olde")  # Backlashes allow continuations...

    # A few special case
    def example6(self):
        if (a == b and c == d and
            d == e and f == g):
            print("new")  # But parentheses usually do too, and are obvious

    # A few special case
    def example7(self):
        x = (1 + 2 + 3      # Omitting the \ makes this very different!
            + 4)
        print(x)

    # A few special case
    def example8(self):
        x = 1; y = 2; print(x)  # More than one simple statement

    # A few special case
    def example9(self):
        S = """
        aaaa
        bbbb
        cccc """

        S = ("aaaa"
             "bbbb"
             "cccc")   # Comments are ignored

        print(S)

    # A few special case
    def example10(self):
        if 1: print("hello")  # Simple statement on header line