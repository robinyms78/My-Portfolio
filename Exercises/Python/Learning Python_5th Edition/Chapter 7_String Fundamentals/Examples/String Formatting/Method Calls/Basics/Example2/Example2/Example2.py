# Same via expression
template = "%s, %s and %s"
print(template %("spam", "ham", "eggs"))

template = "%(motto)s, %(pork)s and %(food)s"
print(template %dict(motto = "spam", pork = "ham", food = "eggs"))

X = "{motto}, {0} and {food}".format(42, motto = "3.14", food = [1,2])
print(X)

Z = X.split(" and ")
print(Z)

Y = X.replace("and", "but under no circumstances")
print(Y)
