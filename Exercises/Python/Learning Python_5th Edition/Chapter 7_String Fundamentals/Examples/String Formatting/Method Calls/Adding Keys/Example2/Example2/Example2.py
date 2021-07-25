somelist = list("SPAM")
print(somelist)

print("first = {0[0]}, third = {0[2]}".format(somelist))

# -1 fails in fmt
print("first = {0}, last = {1}".format(somelist[0], somelist[-1]))

# [1:3] fails in fmt
parts = somelist[0], somelist[-1], somelist[1:3]
print("first = {0}, last = {1}, middle = {2}".format(*parts))


