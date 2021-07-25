class Break():
    def example1(self):
        while True:     # Type Ctrl-C to stop me!
            pass

    # continue
    def example5(self):
        x = 10
        print("\n")
        while x:
            x = x - 1               # Or, x -= 1
            if x % 2 != 0:
                continue            # Odd? -- skip print
            print(x, end = " ")

    # continue
    def example6(self):
        x = 10
        print("\n")
        while x:
            x = x - 1
            if x % 2 == 0:          # Even? -- print
                print(x, end = " ")

    # break
    def example7(self):
        print("\n")
        while True:
            name = input("Enter name: ")   # Use raw_input() in 2.X
            if name == "stop":
                break
            age = input("Enter age: ")
            print("Hello", name, "=>", int(age) ** 2)

    # Loop else
    def example8(self):
        y = 9
        x = y // 2              # For some y > 1
        while x > 1:
            if y % x == 0:      # Remainder
                print(y, "has factor", x)
                break           # Skip else
            x -= 1
        else:                   # Normal exit
            print(y, "is prime")

    # More on the loop else
    def example9(self):
        found = False
        x = "spam"
        while x and not found:
            if match(x[0]):       # Value at front?
                print("Ni")
            else:
                x = x[1:]

        if not found:
            print("not found")

    # More on the loop else
    def example10(self):
        x = "spam"
        while x:                # Exit when x is empty
            if match(x[0]):
                print("Ni")
                break           # Exit, go around else
            x = x[1:]
        else:
            print("Not found")  # Only here if exhausted x






