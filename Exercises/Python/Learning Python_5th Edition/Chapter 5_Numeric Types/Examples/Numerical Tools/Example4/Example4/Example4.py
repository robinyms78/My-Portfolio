﻿import random

print(random.random())
print(random.randint(1, 10))

print(random.choice(["Life of Brian", "Holy Grail", "Meaning of Life"]))
suits = ["hearts", "clubs", "diamonds", "spades"]
random.shuffle(suits)
print(suits)