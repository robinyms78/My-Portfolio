# Search for position
# Occurs at offset 4

S = "xxxxSPAMxxxxSPAMxxxx"
where = S.find("SPAM")
print(where)

S = S[:where] + "EGGS" + S[(where + 4):]
print(S)

# Replace all
S = "xxxxSPAMxxxxSPAMxxxx"
Y = S.replace("SPAM", "EGGS")
print(Y)

# Replace one
S = "xxxxSPAMxxxxSPAMxxxx"
Y = S.replace("SPAM", "EGGS", 1)
print(Y)

