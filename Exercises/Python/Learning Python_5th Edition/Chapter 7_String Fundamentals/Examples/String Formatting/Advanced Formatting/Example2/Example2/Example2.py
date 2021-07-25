x = 1.23456789
print("%e | %f | %g" %(x, x, x))
print("%E" %x)
print("%-6.2f | %05.2f | %+06.1f" %(x, x, x))
print("%s" %x, str(x))
print("%f, %.2f, %.*f" %(1/3.0, 1/3.0, 4, 1/3.0))