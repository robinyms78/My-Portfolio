import sys

class Redirection():
    # Print stream redirection
    def example1(self):
        print("Example1\n")
        print("Hello world")        # Print a string object in 3.X

    # Print stream redirection
    def example2(self):
        print("Example2\n")
        sys.stdout.write("hello world\n")   # Printing the hard way   

    # Automatic stream redirection
    def example3(self):
        print("Example3\n")
        temp = sys.stdout                    # Save the restoring later
        sys.stdout = open("log.txt", "a")    # Redirect prints to a file
        print("spam")                        # Prints go to file, not here
        print(1,2,3)
        sys.stdout.close()                   # Flush output to disk
        sys.stdout = temp                    # Restore original stream
        print("back here")                   # Print show up here again
        print(open("log.txt").read())        # Result of earlier prints

    # Automatic stream redirection
    def example4(self):
        print("Example4\n")
        log = open("log.txt", "w")
        print(1, 2, 3, file = log)
        print(4, 5, 6, file = log)
        log.close()
        print(7, 8, 9)
        print(open("log.txt").read())

    # Automatic stream redirection
    def example5(self):
        print("Example5\n")
        sys.stderr.write(("Bad!" * 8) + "\n")
        print("Bad!" * 8, file = sys.stderr)

    # Automatic stream redirection
    def example6(self):
        print("Example6\n")
        X = 1; Y = 2            # Print the easy way
        print("Example6\n")
        print(X, Y)

        sys.stdout.write(str(X) + " " + str(Y) + "\n")           # Print the hard way
        print(X, Y, file = open("temp1", "w"))                   # Redirect text to file
        open("temp2", "w").write(str(X) + " " + str(Y) + "\n")   # Send to file manually
        print(open("temp1", "rb").read())
        print(open("temp2", "rb").read())                        # Binary mode for bytes



        