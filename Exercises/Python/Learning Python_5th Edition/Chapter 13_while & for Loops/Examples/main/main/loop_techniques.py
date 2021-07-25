class Loop():
    # Counter loops: range
    def example1(self):
        print(list(range(5)))
        print(list(range(2,5)))
        print(list(range(0, 10, 2)))

    # Counter loops: range
    def example2(self):
        print(list(range(-5, 5)))
        print(list(range(5, -5, -1)))

    # Counter loops: range
    def example3(self):
        for i in range(3):
            print(i, "Pythons")

    # Sequence Scans: while and range versus for
    def example4(self):
        X = "spam"
        for item in X:      # Simple iteration
            print(item, end = " ")

    # Sequence Scans: while and range versus for
    def example5(self):
        i = 0
        X = "spam"
        print("\n")
        while i < len(X):   # while loop iteration
            print(X[i], end = " ")
            i += 1

    # Sequence Scans: while and range versus for
    def example6(self):
        X = "spam"
        print("\n")
        print(len(X))               # Length of string
        print(list(range(len(X))))         # All legal offsets into X
        for i in range(len(X)):     # Manual range/len iteration
            print(X[i], end = " ")

    # Sequence Shufflers: range and len
    def example7(self):
        S = "spam"
        print("\n")
        for i in range(len(S)):     # For repeat count 0..3
            S = S[1:] + S[:1]       # Move front item to end
            print(S, end = " ")

    # Sequence Shufflers: range and len
    def example8(self):
        S = "spam"
        print("\n")
        for i in range(len(S)):     # For positions 0..3
            X = S[i:] + S[:i]       # Rear part + front part 
            print(X, end = " ")

    # Sequence Shufflers: range and len
    def example9(self):
        L = [1, 2, 3]
        print("\n")
        for i in range(len(L)):
            X = L[i:] + L[:i]           # Works on any sequence type
            print(X, end = " ")

    # Nonexhaustive Traversals: range versus slices
    def example10(self):
        S = "abcdefghijk"
        print("\n")
        print(list(range(0, len(S), 2)))
        
        for i in range(0, len(S), 2):
            print(S[i], end = " ")

    # Nonexhaustive Traversals: range versus slices
    def example11(self):
        S = "abcdefghijk"
        print("\n")
        for c in S[::2]:
            print(c, end = " ")

    # Changing Lists: range versus comprehensions
    def example12(self):
        print("\n")
        L = [1, 2, 3, 4, 5]
        for x in L:     # Changes X, not L
            x += 1
        print(L)

    # Changing Lists: range versus comprehensions
    def example13(self):
        L = [1, 2, 3, 4, 5]
        for i in range(len(L)):
            L[i] += 1           # Add one to each item in L
        print(L)                # Or L[i] = L[i] + 1


    # Changing Lists: range versus comprehensions
    def example14(self):
        L = [1, 2, 3, 4, 5]
        i = 0
        while i < len(L):
            L[i] += 1
            i += 1
        print(L)

    # Changing Lists: range versus comprehensions
    def example15(self):
        L = [1, 2, 3, 4, 5]
        print([x + 1 for x in L])
            
    # Parallel Traversals: zip and map
    def example16(self):
        L1 = [1, 2, 3, 4]
        L2 = [5, 6, 7, 8]
        print(list(zip(L1, L2)))       # list() required in 3.X, not 2.X

    # Parallel Traversals: zip and map
    def example17(self):
        L1 = [1, 2, 3, 4]
        L2 = [5, 6, 7, 8]
        for (x, y) in zip(L1, L2):
            print(x, y, "--", x + y)

    # Parallel Traversals: zip and map
    def example18(self):
        T1, T2, T3 = (1,2,3), (4,5,6), (7,8,9)
        print(T3)
        print(list(zip(T1, T2, T3)))    # Three tuples for three arguments

    # Parallel Traversals: zip and map
    def example19(self):
        S1 = "abc"
        S2 = "xyz123"
        print(list(zip(S1, S2)))        # Truncates at len(shortest)

    # Map equivalence in Python 2.X
    def example20(self):
        S1 = "abc"
        S2 = "xyz123"
        print(list(map(None, S1, S2)))       # 2.X only: pads to len(longest)

    # Map equivalence in Python 2.X
    def example21(self):
        print(list(map(ord, "spam")))

    # Map equivalence in Python 2.X
    def example22(self):
        res = []
        for c in "spam":
            res.append(ord(c))
        print(res)

    # Dictionary construction with zip
    def example23(self):
        D1 = {"spam": 1, "eggs": 3, "toast": 5}
        print(D1)

    # Dictionary construction with zip
    def example24(self):
        D1 = {}
        D1["spam"] = 1
        D1["eggs"] = 3
        D1["toast"] = 5
        print(D1)

    # Dictionary construction with zip
    def example25(self):
        keys = ["spam", "eggs", "toast"]
        vals = [1, 3, 5]
        print(list(zip(keys, vals)))

    # Dictionary construction with zip
    def example26(self):
        D2 = {}
        keys = ["spam", "eggs", "toast"]
        vals = [1, 3, 5]
        for (k,v) in zip(keys, vals):
            D2[k] = v
        print(D2)

    # Dictionary construction with zip
    def example27(self):
        keys = ["spam", "eggs", "toast"]
        vals = [1, 3, 5]
        D3 = dict(zip(keys, vals))
        print(D3)

    # Dictionary construction with zip
    def example28(self):
        keys = ["spam", "eggs", "toast"]
        vals = [1, 3, 5]
        print({k: v for (k, v) in zip(keys, vals)})

    # Generating Both Offsets and Items: enumerate
    def example29(self):
        S = "spam"
        offset = 0
        for item in S:
            print(item, "appears at offset", offset)
            offset += 1

    # Generating Both Offsets and Items: enumerate
    def example30(self):
        S = "spam"
        for (offset, item) in enumerate(S):
            print(item, "appears at offset", offset)

    # Generating Both Offsets and Items: enumerate
    def example31(self):
        S = "spam"
        E = enumerate(S)
        print(next(E))
        print(next(E))
        print(next(E))

    # Generating Both Offsets and Items: enumerate
    def example32(self):
        S = "spam"
        print([c * i for (i, c) in enumerate(S)])

    # Generating Both Offsets and Items: enumerate
    def example33(self):
        for (i, l) in enumerate(open("Test/test.txt")):
            print("%s) %s" %(i, l.rstrip()))


















