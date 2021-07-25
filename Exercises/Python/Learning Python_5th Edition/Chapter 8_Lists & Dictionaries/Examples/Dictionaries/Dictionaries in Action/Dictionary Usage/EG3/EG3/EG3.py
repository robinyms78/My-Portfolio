Matrix = {}
Matrix[(2,3,4)] = 88
Matrix[(7,8,9)] = 99

# Check for key before fetch
if (2,3,6) in Matrix:
    print(Matrix[(2,3,4)])
else:
    print(0)

# Try to index
# Catch and recover
try:
    print(Matrix[(2,3,6)])
except KeyError:
    print(0)

# Exists: fetch and return
print(Matrix.get((2,3,4), 0))
print(Matrix.get((2,3,6), 0))


