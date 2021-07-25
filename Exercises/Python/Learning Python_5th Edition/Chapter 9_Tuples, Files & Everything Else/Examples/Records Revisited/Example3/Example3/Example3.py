# Import extension type
from collections import namedtuple

# Make a generated class
Rec = namedtuple("Rec", ["name", "age", "jobs"])

# A named-tuple record
bob = Rec("bob", age = 40.5, jobs = ["dev", "mgr"])
print(bob)

# Access by position
print(bob[0], bob[2])

# Access by attribute
print(bob.name, bob.jobs)

# Dictionary-like form
O = bob._asdict()

# Access by key too
print(O["name"], O["jobs"])
print(O)

