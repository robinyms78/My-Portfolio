class C1:
    def setname(self, who):
        self.name = who

# Make two instances
I1 = C1()
I2 = C1()

# Set I1.name to "Bob"
I1.setname("bob")
I2.setname("sue")

# Prints "bob"
print(I1.name)

