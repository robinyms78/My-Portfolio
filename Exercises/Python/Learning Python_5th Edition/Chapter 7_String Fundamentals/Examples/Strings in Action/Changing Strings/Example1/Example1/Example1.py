S = "spam"

# Raises an error
#S[0] = "x"

# To change a string, make a new one
S = S + "SPAM!"
print(S)

S = S[:4] + "Burger" + S[-1]
print(S)

# Replace method
S = "splot"
S = S.replace("pl", "pamal")
print(S)

# Format expression
print("That is %d %s bird!" %(1, "dead")) 

# Format method
print("That is {0} {1} bird!".format(1, "dead"))

