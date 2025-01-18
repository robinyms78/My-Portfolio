import csv
import numpy as np
import itertools

from scipy import linalg
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.mixture import GaussianMixture

def gaussian():
    # Load data from input file
    input_file = "Sales_Transactions_Dataset_Weekly.csv"
    file_reader = csv.reader(open(input_file, "r"), delimiter=",")

    X = []
    for count, row in enumerate(file_reader):
        if not count:
            names = row[1:53]
            continue

        X.append([int(x) for x in row[1:53]])

    array = []
    # Convert to numpy array
    for i in range(len(X)):
        array.append(X[i])
        z = np.array(array)

    # Extract two features for visualization
    plt.figure()
    plt.scatter(z[:,0], z[:,1], marker="o", facecolors="none", edgecolors="black", s=80)
    x_min, x_max = z[:,0].min() - 1, z[:,0].max() + 1
    y_min, y_max = z[:,1].min() -1, z[:,1].max() + 1
    plt.title("Input data")
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks()
    plt.yticks()

    # Create KMeans object
    lowest_bic = np.infty
    bic = []
    n_components_range = range(1, 53)
    cv_types =["spherical", "tied", "diag", "full"]
    for cv_type in cv_types:
        for n_components in n_components_range:
            # Fit a Gaussian mixture with EM
            gmm = GaussianMixture(n_components=n_components, covariance_type = cv_type)
            # Train the KMeans clustering model
            gmm.fit(z)
            bic.append(gmm.bic(z))
            if bic[-1] < lowest_bic:
                lowest_bic = bic[-1]
                #best_gmm = gmm

    bic = np.array(bic)
    color_iter = itertools.cycle(["navy", "turquoise", "cornflowerblue", "darkorange"])
    bars = []

    # Plot the BIC scores
    plt.figure(figsize=(8, 6))
    #spl = plt.subplot(2, 1, 1)
    for i, (cv_type, color) in enumerate(zip(cv_types, color_iter)):
        xpos = np.array(n_components_range) + .2 * (i - 2)
        bars.append(plt.bar(xpos, bic[i * len(n_components_range): (i + 1) * len(n_components_range)], width=.2, color=color))
    plt.xticks(n_components_range)
    plt.ylim([bic.min() * 1.01 - .01 * bic.max(), bic.max()])
    plt.title("BIC score per model")
    xpos = np.mod(bic.argmin(), len(n_components_range)) + .65 + .2 * np.floor(bic.argmin() / len(n_components_range))
    plt.text(xpos, bic.min() * 0.97 + .03 * bic.max(), "*", fontsize=14)
    plt.xlabel("Number of components")
    plt.legend([b[0] for b in bars], cv_types)
    plt.show()