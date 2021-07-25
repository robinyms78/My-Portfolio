# By position
template = "{0}, {1} and {2}"
print(template.format("spam", "ham", "eggs"))

# By keyword
template = "{motto}, {pork} and {food}"
print(template.format(motto = "spam", pork = "ham", food = "eggs"))

# By both
template = "{motto}, {0} and {food}"
print(template.format("ham", motto = "spam", food = "eggs"))

# By relative position
template = "{}, {} and {}"
print(template.format("spam", "ham", "eggs"))
