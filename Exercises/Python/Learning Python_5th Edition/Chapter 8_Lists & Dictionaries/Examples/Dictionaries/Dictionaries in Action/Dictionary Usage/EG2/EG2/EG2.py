Matrix = {}
Matrix[(2,3,4)] = 88
Matrix[(7,8,9)] = 99

# ; separates statements
X = 2; Y = 3; Z = 4
print(Matrix[(X, Y, Z)])
print(Matrix)

# KeyError: (2,3,6)
# print(Matrix[(2,3,6)])

