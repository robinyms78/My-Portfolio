import sys
import docstrings

# The dir Function
def example1():
    print(dir(sys))

# The dir Function
def example2():
    print("\n")
    print(len(dir(sys)))                                                # Number names in sys
    print(len([x for x in dir(sys) if not x.startswith("__")]))         # Non __X names only
    print(len([x for x in dir(sys) if not x[0] == "_"]))                # Non underscore names

# The dir Function
def example3():
    print("\n")
    print(dir([]))
    print(dir(""))
    print(len(dir([])), len([x for x in dir([]) if not x.startswith("__")]))
    print(len(dir("")), len([x for x in dir("") if not x.startswith("__")]))

# The dir Function
def example4():
    print("\n")
    print([a for a in dir(list) if not a.startswith("__")])
    print([a for a in dir(dict) if not a.startswith("__")])

# The dir Function
def example5():
    print("\n")
    def dir1(x):            # See Part IV
        return [a for a in dir(x) if not a.startswith("__")]
    print(dir1(tuple))

# The dir Function
def example6():
    print("\n")
    print(dir(str) == dir(""))     # Same result, type name or literal
    print(dir(list) == dir([]))


# Docstrings: __doc__
def example7():
    print("\n")
    print(docstrings.__doc__)
    print(docstrings.square.__doc__)
    print(docstrings.Employee.__doc__)

# Built-in docstrings
def example8():
    print("\n")
    print(sys.__doc__)
    print(sys.getrefcount.__doc__)
    print(int.__doc__)
    print(map.__doc__)

# PyDoc: The Help Function
def example9():
    print(help(sys.getrefcount))
    #print(help(sys))
    #print(help(dict))
    print(help(str.replace))
    print(help("".replace))
    print(help(ord))


# PyDoc: The Help Function
def example10():
    print("\n")
    print(help(docstrings.square))
    print(help(docstrings.Employee))
    print(help(docstrings))


if __name__ == "__main__":
    example1()
    example2()
    example3()
    example4()
    example5()
    example6()
    example7()
    example8()
    example9()
    example10()












