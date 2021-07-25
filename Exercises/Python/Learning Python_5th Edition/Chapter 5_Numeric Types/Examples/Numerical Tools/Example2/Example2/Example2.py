import math

# Floor (next-lower integer)
print(math.floor(2.567), math.floor(-2.567))

# Truncate (drop decimal digits)
print(math.trunc(2.567), math.trunc(-2.567))

# Truncate (integer conversion)
print(int(2.567), int(-2.567))

# Round(Python 3.X Version)
print(round(2.567), round(2.467), round(2.567, 2))

# Round for display
print("%.1f" %2.567, "{0:.2f}".format(2.567))
print((1/3.0), round(1/3.0, 2), ("%.2f" %(1/3.0)))

