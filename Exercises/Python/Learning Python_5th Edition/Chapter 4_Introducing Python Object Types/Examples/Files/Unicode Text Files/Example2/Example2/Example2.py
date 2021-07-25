import codecs

# Non-ASCII unicode text
S = "sp\xc4m"

# Write/encode UTF-8 text
file = open("unidata.txt", "w", encoding = "utf-8")

# 4 characters written
file.write(S)
file.close()

# Read/encode text
text = codecs.open("unidata.txt", encoding = "utf-8").read()
print(text)

# Read raw bytes
raw = open("unidata.txt", "rb").read()
print(raw)

# Raw/undecoded too
#raw = open("unidata.txt").read()
#print(raw)