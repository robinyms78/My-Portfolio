import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift, estimate_bandwidth

def meanShift():
    # Load data from input file
    input_file = "Sales_Transactions_Dataset_Weekly.csv"
    file_reader = csv.reader(open(input_file, "r"), delimiter=",")

    X = []
    for count, row in enumerate(file_reader):
        if not count:
            names = row[1:53]
            continue

        X.append([float(x) for x in row[1:53]])

    # Convert to numpy array
    X = np.array(X)

    print(X)
    # Estimate the bandwidth of input data
    bandwidth = estimate_bandwidth(X, quantile=0.8, n_samples=len(X))

    # Compute clustering with MeanShift
    meanshift_model = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    meanshift_model.fit(X)

    # Extract labels and centers of each cluster
    labels = meanshift_model.labels_
    cluster_centers = meanshift_model.cluster_centers_
    num_clusters = len(np.unique(labels))

    # Print number of clusters and clusters center
    print("\nNumber of clusters in input data =", num_clusters)
    print("\nCenters of clusters:")
    print("\t".join([str(int(name[1:]) + 1) for name in names]))
    for cluster_center in cluster_centers:
        print("\t".join([str(round(float(x), 3)) for x in cluster_center]))

    # Extract two features for visualization
    cluster_centers_2d = cluster_centers[:, 1:3]

    # Plot the cluster centers
    plt.figure()
    plt.scatter(cluster_centers_2d[:,0], cluster_centers_2d[:,1], s=120, edgecolors="black", facecolors="none")
    offset = 0.25
    plt.xlim(cluster_centers_2d[:,0].min() - offset * cluster_centers_2d[:,0].ptp(),
             cluster_centers_2d[:,0].max() + offset * cluster_centers_2d[:,0].ptp(),)
    plt.ylim(cluster_centers_2d[:,1].min() - offset * cluster_centers_2d[:,1].ptp(),
             cluster_centers_2d[:,1].max() + offset * cluster_centers_2d[:,1].ptp())
    plt.title("Centers of 2D clusters")
    plt.show()
