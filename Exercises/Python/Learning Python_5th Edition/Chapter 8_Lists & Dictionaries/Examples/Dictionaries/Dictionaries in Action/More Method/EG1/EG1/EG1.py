D = {"spam":2, "ham":1, "egg":3}
print(list(D.values()))
print(list(D.items()))

# A key that is there
print(D.get("spam"))

# A key that is missing
print(D.get("toast"))
print(D.get("toast", 88))

# Lots of delicious scrambled order here
D2 = {"toast":4, "muffin":5}
D.update(D2)
print(D)

# Pop a dictionary by key
D.pop("muffin")
D.pop("toast")
print(D)

# Pop a list by position
L = ["aa", "bb", "cc", "dd"]

# Delete and return from the end
L.pop()
print(L)

# Delete from a specific position
L.pop(1)
print(L)



