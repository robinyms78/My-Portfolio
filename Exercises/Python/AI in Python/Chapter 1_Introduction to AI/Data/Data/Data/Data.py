﻿from sklearn import datasets

house_prices = datasets.load_boston()
digits = datasets.load_digits()
print(digits.images[4])
