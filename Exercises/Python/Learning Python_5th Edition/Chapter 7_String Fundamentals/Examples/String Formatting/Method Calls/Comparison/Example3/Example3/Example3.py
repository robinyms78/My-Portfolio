import sys

# Adding specific formatting
print("%-10s = %10s" %("spam", 123.4567))
print("%10s = %-10s" %("spam", 123.4567))
print("%(plat)10s = %(kind)-10s" %dict(plat = sys.platform, kind = "laptop"))

# Floating-point numbers
print("%e, %.3e, %g" %(3.14159, 3.14159, 3.14159))
print("%f, %.2f, %06.2f" %(3.14159, 3.14159, 3.14159))

# Hex and octal, but not binary
print("%x, %o" %(255, 255))