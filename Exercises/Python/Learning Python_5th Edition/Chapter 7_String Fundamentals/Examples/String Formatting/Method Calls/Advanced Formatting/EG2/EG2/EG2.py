import sys

print("{:10} = {:10}".format("spam", 123.4567))
print("{:>10} = {: < 10}".format("spam", 123.4567))
#print("{.platform: > 10} = {[kind]: < 10}".format(sys, dict(kind = "laptop")))
print("{0:e}, {1:.3e}, {2:g}".format(3.14159, 3.14159, 3.14159))
print("{0:f}, {1:.2f}, {2:06.2f}".format(3.14159, 3.14159, 3.14159))