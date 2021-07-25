# Filtering out duplicates (possibility reordered)
print(list(set([1, 2, 1, 3, 1])))

# Finding differences in collections
print(set ("spam") - set("ham"))

# Order-neutral equality
print(set("spam") == set("asmp"))

print("p" in set("spam"), "p" in "spam", "ham" in ["eggs", "spam", "ham"])