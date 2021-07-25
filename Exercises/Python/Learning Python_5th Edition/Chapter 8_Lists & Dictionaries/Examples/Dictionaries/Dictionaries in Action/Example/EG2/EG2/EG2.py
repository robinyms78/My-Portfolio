# Key => Value(title => year)
table = {"Holy Grail": "1975",
         "Life of Brian": "1979",
         "The Meaning of Life": "1983"}
print(table["Holy Grail"])

# Value => Key (year => title)
print(list(table.items()))
print([title for (title, year) in table.items() if year == "1975"])

# Key => Value(normal usage)
K = "Holy Grail"
print(table[K])

# Value => Key
V = "1975"
print([key for (key,value) in table.items() if value == V])

# Ditto
print([key for key in table.keys() if table[key] == V])


