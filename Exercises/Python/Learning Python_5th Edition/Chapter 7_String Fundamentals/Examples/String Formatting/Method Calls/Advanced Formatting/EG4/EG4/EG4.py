# Parameters hardcoded
print("{0:.2f}".format(1/3.0))

# Ditto for expression
print("%.2f"%(1/3.0))

# Take value from arguments
print("{0:.{1}f}".format(1/3.0, 4))

# Ditto for expression
print("%.*f" %(4, 1/3.0))