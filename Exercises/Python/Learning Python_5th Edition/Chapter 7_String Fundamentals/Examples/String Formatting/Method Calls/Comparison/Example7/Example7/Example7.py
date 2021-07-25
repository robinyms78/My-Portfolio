from formats import commas

X = [commas(x) for x in (9999999, 8888888)]
print(X)
print("%s %s" %tuple(commas(x) for x in (9999999, 8888888)))
print("".join(commas(x) for x in (9999999, 8888888)))
