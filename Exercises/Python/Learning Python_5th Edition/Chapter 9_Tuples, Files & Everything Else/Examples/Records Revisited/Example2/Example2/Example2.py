# Dictionary record
bob = dict(name = "Bob", age = 40.5, jobs = ["dev", "mgr"])
print(bob)

# Access by key
print(bob["name"], bob["jobs"])

# Values to tuple
X = tuple(bob.values())
print(X)

# Items to tuple list
Y = list(bob.items())
print(Y)

