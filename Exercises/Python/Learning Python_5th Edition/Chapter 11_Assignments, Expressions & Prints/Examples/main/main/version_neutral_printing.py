class Neutral():
    # Version-neutral printing
    def example1(self):
        print("Example1\n")
        print("spam")                   #3.X print function call syntax
        print("spam", "ham", "eggs")    # These are multiple arguments

    # Version-neutral printing
    def example2(self):
        print("Example2\n")
        print()                         # This is just a line-feed on 3.X

    # Version-neutral printing
    def example3(self):
        print("Example3\n")
        print("%s %s %s" %("spam", "ham", "eggs"))
        print("{0} {1} {2}".format("spam", "ham", "eggs"))
        print("answer: " + str(42))

