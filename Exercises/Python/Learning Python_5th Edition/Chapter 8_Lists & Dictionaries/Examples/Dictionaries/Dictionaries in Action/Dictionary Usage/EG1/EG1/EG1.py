L = []
# L[99] = "spam"

D = {}
D[99] = "spam"
print(D[99])
print(D)

# Keys are integers, not strings
table = {1975: "Holy Grail",
         1979: "Life of Brian",
         1983: "The Meaning of Life"}
print(table[1975])
print(list(table.items()))