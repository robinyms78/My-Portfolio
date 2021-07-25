# Zip together keys and values
L =list(zip(["a", "b", "c"], [1, 2, 3]))
print(L)

# Make a dict from zip result
D = dict(zip(["a", "b", "c"], [1, 2, 3]))
print(D)

D = {k: v for (k,v) in zip(["a", "b", "c"], [1, 2, 3])}
print(D)

# Or: range(1,5)
D = {x: x ** 2 for x in [1, 2, 3, 4]}
print(D)

D = {c.lower(): c + "!" for c in ["SPAM", "EGGS", "HAM"]}
print(D)

# Initialize dict from keys
D = dict.fromkeys(["a", "b", "c"], 0)
print(D)

# Same, but with a comprehension
D = {k: 0 for k in ["a", "b", "c"]}
print(D)

# Other iterables, default value
D = dict.fromkeys("spam")
print(D)
D = {k: None for k in "spam"}
print(D)




