L = ["spam", "eggs", "ham", "toast"]

# Delete one item
del L[0]
print(L)

# Delete an entire section
# Same as L[1:] = []
del L[1:]
print(L)

L = ["Already", "got", "one"]
L[1:] = []
print(L)
L[0] = []
print(L)




