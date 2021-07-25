from fractions import Fraction

print(4.0/3)

# Precision loss from float
print((4.0/3).as_integer_ratio())

x = Fraction(1,3)
a = x + Fraction(*(4.0/3).as_integer_ratio())
print(a)

# 5/3(or close to it!)
print(22517998136852479/13510798882111488.)

# Simplify to closest fraction
print(a.limit_denominator(10))