# Define a class object
class FirstClass:
    # Define class's methods
    def setdata(self, value):
        self.data = value
    def display(self):
        # self.data: per instance
        print(self.data)

# Make two instances
# Each is a new namespace
x = FirstClass()
y = FirstClass()

# Call methods: self is x
x.setdata("King Arthur")
y.setdata(3.14159)

# self.data differs in each instance
x.display()

# Runs: FirstClass.display(y)
y.display()

# Can get/set attributes out the class too
x.data = "New value"
x.display()

# Can set new attributes here too!
x.anothername = "spam"


# Inherits setdata
class SecondClass(FirstClass):
    # Changes display
    def display(self):
        print("current value = '%s'" %self.data)

# Finds setdata in FirstClass
z = SecondClass()
z.setdata(42)

# Finds overridden method in second class
z.display()

# Inherit from SecondClass
# On ThirdClass(value)
class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    # On "self + other"
    def __add__(self, other):
        return ThirdClass(self.data + other)

    # On "print(self)", "str()"
    def __str__(self):
        return "[ThirdClass: %s]" % self.data

    # In-place change: named
    def mul(self, other):
        self.data *= other

# __init__called
a = ThirdClass("abc")

# Inherited method called
a.display()

# __str__: returns display string
print(a)

#__add__: makes a new instance
b = a + "xyz"

# b has all ThirdClass methods
b.display()

# __str__: returns display string
print(b)

# mul: changes instance in place
a.mul(3)
print(a)





























