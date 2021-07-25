class Print():
    # The Python 3.X print function 
    def example1(self):
        print("Example1\n")
        print()                 # Display a blank line

        x = "spam"
        y = 99
        z = ["eggs"]
        print("\n")
        print(x, y, z)          # Print three objects per defaults

    # The Python 3.X print function
    def example2(self):
        x = "spam"
        y = 99
        z = ["eggs"]
        print("Example2\n")
        print(x, y, z, sep = "")    # Suppress separator
        print("\n")
        print(x, y, z, sep = ",")   # Custom separator
        print("\n")
        print(x, y, x, end = "")    # Suppress line break
        print("\n")
        print(x, y, z, end = ""); print(x,y,z)    # Two prints, same output line
        print("\n")
        print(x, y, z, end = "...\n")  # Custom line end
        print("\n")
        print(x, y, z, sep = "...", end = "!\n")    # Multiple keywords
        print("\n")
        print(x, y, z, end = "!\n", sep = "...")    # Order doesn't matter

    # The Python 3.X print function
    def example3(self):
        x = "spam"
        y = 99
        z = ["eggs"]
        print("Example3\n")
        print(x, y, z, sep = "...", file = open("data.txt", "w"))   # Print to a file
        print(x, y, z)  # Back to stdout
        print("\n")
        print(open("data.txt").read())  # Display file text

    # The Python 3.X print function
    def example4(self):
        text = "%s: %-.4f, %05d" %("Result", 3.14159, 42)
        print("Example4\n")
        print(text)
        print("\n")
        print("%s: %-.4f, %05d" %("Result", 3.14159, 42))


