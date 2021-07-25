# Import extension type
from collections import namedtuple

# Make a generated class
Rec = namedtuple("Rec", ["name", "age", "jobs"])

# For both tuples and named tuples
bob = Rec("Bob", 40.5, ["dev", "mgr"])

# Tuple assignment
name, age, jobs = bob
print(name, jobs)


