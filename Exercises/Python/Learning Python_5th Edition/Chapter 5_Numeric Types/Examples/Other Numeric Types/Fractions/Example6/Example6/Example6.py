from fractions import Fraction

# Float object method
print((2.5).as_integer_ratio())

# Convert float -> fraction: two args
# Same as fraction (5,2)
f = 2.5
z = Fraction(*f.as_integer_ratio())
print(z)

# x from prior interaction
x = Fraction(1,3)

# 5/2 + 1/3 = 15/6 + 2/6
print(x + z)

# Convert fraction -> float
print(float(x))
print(float(z))
print(float(x + z))
print(17/6)

# Convert float -> fraction: other way
print(Fraction.from_float(1.75))
print(Fraction(*(1.75).as_integer_ratio()))




