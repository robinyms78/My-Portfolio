rec = {}
rec["name"] = "Bob"
rec["age"] = 40.5
rec["job"] = "developer/manager"
print(rec["name"])

rec = {"name": "Bob",
       "jobs": ["developer", "manager"],
       "web": "www.bobs.org/~Bob",
       "home": {"state": "overworked",
                "zip": 12345}}
print(rec["name"])
print(rec["jobs"])
print(rec["jobs"][1])
print(rec["home"]["zip"])

# A list "database"
db = []
db.append(rec)
# db.append(other)
print(db[0]["jobs"])

# A dictionary "database"
db = {}
db["bob"] = rec
# db["Sue"] = other
print(db["bob"]["jobs"])





