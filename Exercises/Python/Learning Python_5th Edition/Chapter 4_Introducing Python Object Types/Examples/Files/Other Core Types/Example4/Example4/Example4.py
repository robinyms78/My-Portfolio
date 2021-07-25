# Decimals: fixed precision
import decimal

d = decimal.Decimal("3.141")
print(d + 1)

decimal.getcontext().prec = 2
print(decimal.Decimal("1.00")/decimal.Decimal("3.00"))
