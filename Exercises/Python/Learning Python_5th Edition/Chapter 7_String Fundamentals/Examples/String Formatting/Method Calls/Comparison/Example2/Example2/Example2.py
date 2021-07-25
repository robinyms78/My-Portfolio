import sys

# Arbitrary types
print("%s, %s and %s" %(3.14, 42, [1,2]))

print("My %(kind)s runs %(platform)s" %{"kind":"laptop", "platform":sys.platform})

print("My %(kind)s runs %(platform)s" %dict(kind = "laptop", platform = sys.platform))

somelist = list("SPAM")
parts = somelist[0], somelist[-1], somelist[1:3]
print("first = %s, last = %s, middle = %s" %parts)                            