from decimal import Decimal
import decimal

# Default: 28 digits
print(decimal.Decimal(1) / decimal.Decimal(7))

# Fixed precision
decimal.getcontext().prec = 4
print(decimal.Decimal(1) / decimal.Decimal(7))

# Closer to 0
print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3))
