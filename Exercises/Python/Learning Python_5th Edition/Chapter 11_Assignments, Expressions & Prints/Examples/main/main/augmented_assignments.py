class Augmented():
    # Augmented assignment 
    def example1(self):
        x = 1               # Traditional
        x = x + 1
        print("Example1\n")
        print(x)

        x += 1              # Augmented
        print("\n")
        print(x)

        S = "spam"          # Implied concatenation
        S += "SPAM"
        print("\n")
        print(S)

    # Augmented assignment 
    def example2(self):
        L = [1, 2]
        L = L + [3]         # Concatenate: slower
        print("Example2\n")
        print(L)

        L.append(4)         # Faster, but in place
        print("\n")
        print(L)

        L = L + [5, 6]      # Concatenate: slower
        print("\n")
        print(L)

        L.extend([7, 8])    # Faster, but in place
        print("\n")
        print(L)

        L += [9, 10]        # Mapped to L.extend([9, 10])
        print("\n")
        print(L)

    # Augmented assignment 
    def example3(self):
        L = []              # += and extend allow any sequence, but + does not!
        L += "spam"
        print("Example3\n")
        print(L)

        # L = L + "spam"      # TypeError: can only concatenate list(not "str") to list

    # Augmented assignment and shared references
    def example4(self):
        L = [1, 2]
        M = L                 # L and M reference the same object
        L = L + [3,4]         # Concatenation makes a new object
        print("Example4\n")   # Changes L but not M
        print(L, M)

        L = [1, 2]
        M = L
        L += [3,4]            # But += really means extend
        print("\n")
        print(L, M)           # M sees the in-place change too!