class Worker:
    # Initialize when created
    # Self is the new object
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    
    # Split string on blanks
    def lastName(self):
        return self.name.split()[-1]

    # Update pay in place
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

# Make two instances
bob = Worker("Bob Smith", 50000)
sue = Worker("Sue Jones", 60000)

# Call method: bob is self
print(bob.lastName())

# Sue is the self subject
print(sue.lastName())

# Updates Sue's pay
sue.giveRaise(.10)
print(sue.pay)


