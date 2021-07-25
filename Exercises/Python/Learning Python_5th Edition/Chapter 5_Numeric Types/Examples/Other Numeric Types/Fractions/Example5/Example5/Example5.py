print(1/3)

from fractions import Fraction
from decimal import Decimal

# Numeric accuracy, two ways
print(Fraction(1, 3))

import decimal
decimal.getcontext().prec = 2
print(Decimal(1) / Decimal(3))
print((1/3) + (6/12))

# Automatically simplified
print(Fraction(6, 12))
print(Fraction(1, 3) + Fraction(6, 12))
print(decimal.Decimal(str(1/3)) + decimal.Decimal(str(6/12)))
print(1000.0 / 1234567890)

# Substantially simpler!
print(Fraction(1000, 1234567890))
