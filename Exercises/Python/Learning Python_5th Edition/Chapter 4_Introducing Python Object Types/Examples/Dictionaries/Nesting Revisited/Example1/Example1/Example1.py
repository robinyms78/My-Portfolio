rec = {"name": {"first": "Bob", "last": "Smith"}, "jobs": ["dev","mgr"], "age": 40.5}

# "name" is a nested dictionary
print(rec["name"])

# Index the nested dictionary
print(rec["name"]["last"])

# "jobs" is a nested list
print(rec["jobs"])

# Index the nested list
print(rec["jobs"][-1])

# Expand Bob's job description in place
rec["jobs"].append("janitor")
print(rec)
