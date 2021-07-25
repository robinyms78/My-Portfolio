# 3.X: equality works but magnitude does not
print(11 == "11")
# print(11 >= "11")

# Ditto for sorts
["11", "22"].sort()
# print([11, "11"].sort())

# Mixed numbers convert to highest type
print(11 > 9.123)

# Manual conversions force the issue
print(str(11) >= "11", 11 > int("11"))