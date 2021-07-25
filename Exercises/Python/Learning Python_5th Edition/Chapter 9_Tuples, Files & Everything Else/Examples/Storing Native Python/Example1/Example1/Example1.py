D = {"a": 1, "b": 2}
F = open("datafile.pk1", "wb")

import pickle
# Pickle any object to file
pickle.dump(D, F)
F.close()

# Load any object from file
F = open("datafile.pk1", "rb")
E = pickle.load(F)
print(E)

# Format is prone to change!
print(open("datafile.pk1", "rb").read())

