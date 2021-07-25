L = ["spam", "Spam", "SPAM!"]

# Index assignment
L[1] = "eggs"
print(L)

# Slice assignment: delete + insert
# Replaces iems 0, 1
L[0:2] = ["eat", "more"]
print(L)

# Replacement/insertion
L = [1,2,3]
L[1:2] = [4, 5]

# Insertion(replace nothing)
L[1:1] = [6,7]
print(L)

# Deletion(insert nothing)
L[1:2] = []
print(L)

# Insert all at :0, an empty slice at front
L = [1]
L[:0] = [2,3,4]
print(L)

# Insert all at len(L):, an empty slice at end
L[len(L):] = [5,6,7]
print(L)

# Insert all at end, named method
L.extend([8,9,10])
print(L)

