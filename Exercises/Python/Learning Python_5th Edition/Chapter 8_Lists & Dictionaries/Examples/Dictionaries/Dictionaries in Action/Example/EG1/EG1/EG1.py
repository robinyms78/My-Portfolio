# Key: Value
table = {"1975": "Holy Grail",
         "1979": "Life of Brian",
         "1983": "The Meaning of Life"}

# Dictionary[key] => Value
year = "1983"
movie = table[year]
print(movie)

# Same as: for year in table.keys()
for year in table:
    print(year + "\t" + table[year])



