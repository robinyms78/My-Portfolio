import decimal

# This has more digits in memory than displayed in 3.3
print(1999 + 1.33)

decimal.getcontext().prec = 2
pay = decimal.Decimal(str(1999 + 1.33))
print(pay)

