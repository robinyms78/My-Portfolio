S = "spammy"
L = list(S)
print(L)

# Works for lists, not strings
L[3] = "x"
L[4] = "x"
print(L)

S = "".join(L)
print(S)

Y = "SPAM".join(["eggs", "sausage", "ham", "toast"])
print(Y)

