# 3.X/2.7 set comprehension
print({x ** 2 for x in [1,2,3,4]})

# Same as: set("spam")
print({x for x in "spam"})

# Set of collected expression results
print({c * 4 for c in "spam"})
print({c * 4 for c in "spamham"})

S = {c * 4 for c in "spam"}
print(S | {"mmmm", "xxxx"})
print(S & {"mmmm", "xxxx"})


