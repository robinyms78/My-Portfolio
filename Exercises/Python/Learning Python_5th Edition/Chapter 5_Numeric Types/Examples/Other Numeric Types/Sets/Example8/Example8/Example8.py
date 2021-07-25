engineers = {"bob", "sue", "ann", "vic"}
managers = {"tom", "sue"}

# Is bob an engineer?
print("bob" in engineers)

# Who is both engineer and manager?
print(engineers & managers)

# All people in either category
print(engineers | managers)

# Engineers who are not managers
print(engineers - managers)

# Managers who are not engineers
print(managers - engineers)

# Are all managers engineers? (superset)
print(engineers > managers)

# Are both engineers (subset)
print({"sue", "bob"} < engineers)

# All people is a superset of managers
print((managers | engineers) > managers)

# Who is in one but not both?
print(managers ^ engineers)

# Intersection!
print((managers | engineers) - (managers ^ engineers))