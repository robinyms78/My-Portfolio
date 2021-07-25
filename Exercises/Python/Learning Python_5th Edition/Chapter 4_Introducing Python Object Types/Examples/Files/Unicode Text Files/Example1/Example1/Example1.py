# Non-ASCII unicode text
S = "sp\xc4m"
print(S)

# Sequence of characters
print(S[2])

# Write/encode UTF-8 text
file = open("unidata.txt", "w", encoding = "utf-8")

# 4 characters written
file.write(S)

file.close()

# Read/decode UTF-8 text
text = open("unidata.txt", encoding = "utf-8").read()
print(text)

# 4 chars(code points)
print(len(text))

# Read raw encoded bytes
raw = open("unidata.txt", "rb").read()
print(raw)

# Really 5 bytes in UTF-8
print(len(raw))

# Manual encode to bytes
print(text.encode("utf-8"))

# Manual decode to str
print(raw.decode("utf-8"))

# Bytes differ in others
print(text.encode("latin-1"))
print(text.encode("utf-16"))
print(len(text.encode("latin-1")), len(text.encode("utf-16")))
print(b"\xff\xfes\x00p\x00\xc4\x00m\x00".decode("utf-16"))


