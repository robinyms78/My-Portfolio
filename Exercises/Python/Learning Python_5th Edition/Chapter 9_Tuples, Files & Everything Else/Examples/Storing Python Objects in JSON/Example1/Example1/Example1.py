name = dict(first = "Bob", last = "Smith")
rec = dict(name = name, job = ["dev", "mgr"], age = 40.5)
print(rec)

import json
json.dumps(rec)
S = json.dumps(rec)
print(S)
O = json.loads(S)
print(O)
print(O == rec)

json.dump(rec, fp=open("testjson.txt", "w"), indent = 4)
print(open("testjson.txt").read())
P = json.load(open("testjson.txt"))
print(P)

