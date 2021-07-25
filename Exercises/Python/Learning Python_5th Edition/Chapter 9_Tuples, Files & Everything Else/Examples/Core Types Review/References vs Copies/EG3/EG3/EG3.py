# Embed copies of X's object
X = [1, 2, 3]
L = ["a", X[:], "b"]
D = {"x": X[:], "y": 2}

X[1] = "surprise"
print(L)
print(D)


