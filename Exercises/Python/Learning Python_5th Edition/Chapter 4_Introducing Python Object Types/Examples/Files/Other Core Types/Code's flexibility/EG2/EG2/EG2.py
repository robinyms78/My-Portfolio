L = [None] * 100

# Type testing, if you must...
if type(L) == type([]):
    print("yes")

# Using the type name
if type(L) == list:
    print("yes")

# Object-oriented tests
if isinstance(L, list):
    print("yes")

