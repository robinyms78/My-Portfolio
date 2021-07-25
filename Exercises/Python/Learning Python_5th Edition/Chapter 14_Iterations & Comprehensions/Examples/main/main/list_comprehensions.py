class Comprehensions():
    def example1(self):
        print("\n")
        L = [1, 2, 3, 4, 5]
        for i in range(len(L)):
            L[i] += 10
        print(L)

    def example2(self):
        print("\n")
        L = [1, 2, 3, 4, 5]
        L = [x + 10 for x in L]
        print(L)

    # List Comprehension Basics
    def example3(self):
        print("\n")
        res = []
        L = [1, 2, 3, 4, 5]
        for x in L:
            res.append(x + 10)
        print(res)

    # Using List Comprehensions on Files
    def example4(self):
        print("\n")
        f = open("script2.py")
        lines = f.readlines()
        print(lines)

    # Using List Comprehensions on Files
    def example5(self):
        print("\n")
        f = open("script2.py")
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        print(lines)

    # Using List Comprehensions on Files
    def example6(self):
        print("\n")
        lines = [line.rstrip() for line in open("script2.py")]
        print(lines)

    # Using List Comprehensions on Files
    def example7(self):
        print("\n")
        print([line.upper() for line in open("script2.py")])

    # Using List Comprehensions on Files
    def example8(self):
        print("\n")
        print([line.rstrip().upper() for line in open("script2.py")])

    # Using List Comprehensions on Files
    def example9(self):
        print("\n")
        print([line.split() for line in open("script2.py")])

    # Using List Comprehensions on Files
    def example10(self):
        print("\n")
        print([line.replace(" ", "!") for line in open("script2.py")])

    # Using List Comprehensions on Files
    def example11(self):
        print("\n")
        print([("sys" in line, line[:5]) for line in open("script2.py")])
        
    # Extended List Comprehension Syntax
    def example12(self):
        print("\n")
        lines = [line.rstrip() for line in open("script2.py") if line[0] == "p"]
        print(lines)

    # Extended List Comprehension Syntax
    def example13(self):
        res = []
        print("\n")
        for line in open("script2.py"):
            if line[0] == "p":
                res.append(line.rstrip())
        print(res)

    # Extended List Comprehension Syntax
    def example14(self):
        print("\n")
        print([line.rstrip() for line in open("script2.py") if line.rstrip()[-1].isdigit()])

    # Extended List Comprehension Syntax
    def example15(self):
        print("\n")
        fname = r"E:\Self-Learning\References\Python\Textbooks\Learning Python\Learning Python_5th Edition\Chapter 14_Iterations & Comprehensions\main\main\Test\test.txt"
        print(len(open(fname).readlines()))         # All lines
        print(len([line for line in open(fname) if line.strip() != ""]))      # Non-blank lines

    # Extended List Comprehension Syntax
    def example16(self):
        print("\n")
        print([x + y for x in "abc" for y in "lmn"])

    # Extended List Comprehensions Syntax
    def example17(self):
        print("\n")
        res = []
        for x in "abc":
            for y in "lmn":
                res.append(x + y)
        print(res)

