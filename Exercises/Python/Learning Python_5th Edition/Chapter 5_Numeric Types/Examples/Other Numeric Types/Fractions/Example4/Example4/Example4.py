# This should be zero (close, but not exact)
print(0.1 + 0.1 + 0.1 - 0.3)

from fractions import Fraction
print(Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10))

from decimal import Decimal
print(Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.3"))

 
