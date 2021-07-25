class C1:
    # Set name when constructed
    def __init__(self, who):
        # Self is either I1 or I2
        self.name = who

# Set I1.name to "bob"
I1 = C1("bob")

# Set I2.name to "sue"
I2 = C1("sue")

# Prints ("bob")
print(I1.name)


