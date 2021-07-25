line = "The knights who say Ni!\n"
line.find("Ni") != -1

# Search via method call or expression
print("Ni" in line)

# End test via method call or slice
sub = "Ni!\n"
print(line.endswith(sub))
print(line[-len(sub):] == sub)

