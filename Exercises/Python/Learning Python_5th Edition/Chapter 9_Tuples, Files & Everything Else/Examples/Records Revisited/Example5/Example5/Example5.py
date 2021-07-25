# Dict equivalent (but order may vary)
bob = {"name": "Bob", "age": 40.5, "jobs": ["dev", "mgr"]}
job, name, age = bob.values()
print(name, job, age)

# Step through keys, index values
for x in bob:
    print(bob[x])

# Step through values view
for x in bob.values():
    print(x)


