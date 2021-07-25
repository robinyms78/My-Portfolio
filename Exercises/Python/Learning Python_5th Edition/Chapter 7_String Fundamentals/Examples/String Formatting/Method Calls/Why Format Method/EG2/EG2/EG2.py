print("{name} {job} {name}".format(name = "Bob", job = "dev"))
print("%(name)s %(job)s %(name)s" % dict(name = "Bob", job = "dev")) 

# Method, key references
D = dict(name = "Bob", job = "dev")
print("{0[name]} {0[job]} {0[name]}".format(D))

# Method, dict-to-args
print("{name} {job} {name}".format(**D))

# Expression, key references
print("%(name)s %(job)s %(name)s" %D)