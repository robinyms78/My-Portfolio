﻿from fractions import Fraction

x = Fraction (1,3)

# Fraction + int -> Fraction
print(x + 2)

# Fraction + float -> float
print(x + 2.0)

# Fraction + float -> float
print(x + (1./3))
print(x + (4./3))

# Fraction + Fraction -> Fraction
print(x + Fraction(4,3))

