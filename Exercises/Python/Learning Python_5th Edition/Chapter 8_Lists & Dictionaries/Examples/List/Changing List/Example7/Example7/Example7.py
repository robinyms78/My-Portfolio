# Add many items at end
L = [1,2]
L.extend([3,4,5])
print(L)

# Delete and return last item (by defaul: -1)
L.pop()
print(L)

# In-place reversal method
L.reverse()
print(L)

# Reversal built-in with a result(iterator)
X = list(reversed(L))
print(X)

# Push onto stack
L = []
L.append(1)
L.append(2)
print(L)

# Pop-off stack
L.pop()
print(L)

# Index of an object (search/find)
L = ["spam", "eggs", "ham"]
print(L.index("eggs"))

# Insert at position
L.insert(1, "toast")
print(L)

# Delete by value
L.remove("eggs")
print(L)

# Delete by position
L.pop(1)
print(L)

# Number of occurences
print(L.count("spam"))













