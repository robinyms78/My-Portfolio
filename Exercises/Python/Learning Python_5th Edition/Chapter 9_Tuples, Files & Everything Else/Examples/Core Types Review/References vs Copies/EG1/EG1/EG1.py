# Embed references to X's object
X = [1, 2, 3]
L = ["a", X, "b"]
D = {"x": X, "y": 2}

# Changes all three references
X[1] = "surprise"
print(L)
print(D)

