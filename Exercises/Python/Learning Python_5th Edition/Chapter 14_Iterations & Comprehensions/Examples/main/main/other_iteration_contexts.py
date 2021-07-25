import functools, operator

class Contexts():
    def example1(self):
        print("\n")
        for line in open("script2.py"):     # Use file iterator
            print(line.upper(), end = "")

    def example2(self):
        print("\n")
        uppers = [line.upper() for line in open("script2.py")]
        print(uppers)

    def example3(self):
        print("\n")
        print(map(str.upper, open("script2.py")))    # map is itself an iterable in 3.X
        print(list(map(str.upper, open("script2.py"))))  

    def example4(self):
        print("\n")
        print(sorted(open("script2.py")))

    def example5(self):
        print("\n")
        print(list(zip(open("script2.py"), open("script2.py"))))

    def example6(self):
        print("\n")
        print(list(filter(bool, open("script2.py"))))     # non-empty = True

    def example7(self):
        print("\n")
        print(functools.reduce(operator.add, open("script2.py")))

    def example8(self):
        print("\n")
        print(list(open("script2.py")))

    def example9(self):
        print("\n")
        print(tuple(open("script2.py")))

    def example10(self):
        print("\n")
        print("&&".join(open("script2.py")))

    def example11(self):
        print("\n")
        a, b, c, d = open("script2.py")     # Sequence assignment
        print(a, d)

    def example12(self):
        print("\n")
        a, *b = open("script2.py")          # 3.X extended form
        print(a, b)

    def example13(self):
        print("\n")
        print("y = 2\n" in open("script2.py"))     # Membership test
        print("x = 2\n" in open("script2.py"))

    def example14(self):
        print("\n")
        L = [11, 22, 33, 44]        # Slice assignment
        L[1:3] = open("script2.py")
        print(L)

    def example15(self):
        print("\n")
        L = [11]
        L.extend(open("script2.py"))    # list.extend method
        print(L)

    def example16(self):
        print("\n")
        L = [11]
        L.append(open("script2.py"))    # list.append does not iterate
        print(L)
        print(list(L[1]))

    def example17(self):
        print("\n")
        print(set(open("script2.py")))

    def example18(self):
        print("\n")
        print({line for line in open("script2.py")})

    def example19(self):
        print("\n")
        print({ix: line for ix, line in enumerate(open("script2.py"))})

    def example20(self):
        print("\n")
        print({line for line in open("script2.py") if line[0] == "p"})

    def example21(self):
        print("\n")
        print({ix: line for (ix, line) in enumerate(open("script2.py")) if line[0] == "p"})

    def example22(self):
        print("\n")
        print(list(line.upper() for line in open("script2.py")))

    def example23(self):
        print("\n")
        print(sum([3, 2, 4, 1, 5, 0]))      # sum expects numbers only

    def example24(self):
        print("\n")
        print(any(["spam", "", "ni"]))

    def example25(self):
        print("\n")
        print(all(["spam", "", "ni"]))

    def example26(self):
        print("\n")
        print(max([3, 2, 5, 1, 4]))

    def example27(self):
        print("\n")
        print(min([3, 2, 5, 1, 4]))

    def example28(self):
        print("\n")
        print(max(open("script2.py")))      # Line with max/min strin value
        print(min(open("script2.py")))

    def example29(self):
        print("\n")
        def f(a, b, c, d):
            print(a, b, c, d, sep = "&")
        f(1, 2, 3, 4)
        f(*[1, 2, 3, 4])                # Unpacks into arguments
        f(*open("script2.py"))          # Iterates by lines too!

    def example30(self):
        print("\n")
        X = (1, 2)
        Y = (3, 4)
        print(list(zip(X, Y)))      # Zip tuples: returns an iterable

    def example31(self):
        print("\n")
        X = (1, 2)
        Y = (3, 4)
        A, B = zip(*zip(X, Y))      # Unzip a zip!
        print(A)
        print(B)
