# Shouldn't this be true?
print(1.1 + 2.2 == 3.3)

# Close to 3.3, but not exactly: limited precision
print(1.1 + 2.2)

# OK if convert
print(int(1.1 + 2.2) == int(3.3))

