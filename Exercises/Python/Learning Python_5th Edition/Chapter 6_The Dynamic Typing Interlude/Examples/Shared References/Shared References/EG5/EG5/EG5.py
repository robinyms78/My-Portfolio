x = 42
y = 42

# Should be two different objects
print(x == y)

# Same object anyhow: caching at work!
print(x is y)
