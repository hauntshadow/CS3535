"""
seg_kmeans.py

This code performs K-Means clustering on a dataset passed in as a pickled
NumPy array.

There is a function (seg_kmeans) that performs K-Means on
the dataset not using another class's stuff.  There is another function
(KMeans) that performs K-Means on the dataset by using Scikit-Learn's
K-Means class inside of the cluster package.
Both functions have the follwoing parameters:

    1. filename: the file that contains the dataset (must be a pickled array)
    2. clusters: the number of clusters to generate
    3. iter: the max number of iterations to use

This also saves the results to an output in the Results folder.

Author: Chris Smith

Version: 4.19.2015
"""
import matplotlib
matplotlib.use("Agg")
import numpy as np
from numpy import random
import scipy.spatial.distance as distance
from sklearn import metrics
from sklearn import cluster
import matplotlib.pyplot as plt
import time

'''
Figures out which cluster center that the segment x is closest to.
'''
def classify(x, size, centroids):
    list = np.zeros(size)
    for i in range(size):
        list[i] = np.sqrt(np.sum((centroids[i] - x) ** 2))
    return np.argmin(list)
'''
Figures out the cluster member counts and the max distances from the centers in each cluster.
Also, histograms are generated.
'''
def score(centers, centroids):
    counts = np.zeros(len(centers))
    maxes = np.zeros(len(centers))
    index = 0
    np.asarray(centers)
    for i in range(len(centers)):
        counts[index] = len(centers[index])
        index += 1
    for i in range(len(centers)):
        maxes[i] = distance.cdist(centers[i], np.asarray(centroids[i]).reshape((1,27)), 'euclidean').max()
    if np.amax(counts)/50 >= 5:
        bins = np.amax(counts) / 50
    else:
        bins = 5
    plt.hist(counts.ravel(), bins = bins)
    plt.title('Number of members per cluster')
    plt.xlabel('Number of members')
    plt.ylabel('Number of occurrences')
    ticks = range(0, int(np.amax(counts)))
    plt.xticks(ticks[0::50])
    plt.gcf().savefig('Results/countHistogram.png')
    plt.close()
    if np.amax(maxes)/50 >= 5:
        bins = np.amax(maxes) / 50
    else:
        bins = 5
 
    plt.hist(maxes.ravel(), bins = bins)
    plt.title('Max distance in cluster')
    plt.xlabel('Max distances')
    plt.ylabel('Number of occurrences')
    ticks = range(0, int(np.amax(maxes)))
    plt.xticks(ticks[0::50])
    plt.gcf().savefig('Results/maxdistHistogram.png')
    plt.close()


    print "Counts of each cluster:"
    print counts
    print "------------------------------"
    print "The max distance from each center to a cluster member:"
    print maxes
    print "------------------------------"

'''
Performs K-Means clustering on a dataset of music segments without using a pre-made function.
Saves the results to a .npy file in the Results folder.
'''
def seg_kmeans(filename, clusters, iter):
    #Initialize everything
    data = np.load(filename)
    #Use the first 1 million segments
    data.resize(1000000,27)
    centroids = np.empty((clusters, 27))
    copyroids = np.empty((clusters, 27))
    for i in range(0, clusters):
        sample = random.randint(0, len(data))
        centroids[i] = data[sample]
    #Start the algorithm
    stop = False
    attempt = 1
    numlist = []
    while not stop and attempt <= iter:
        #Initialize the lists
        numlist = []
        for i in range(clusters):
            numlist.append([])
        print "Attempt Number: %d" % attempt
        #Classify stuff
        for row in range(len(data)):
            closest = classify(data[row], clusters, centroids)
            numlist[closest].append(data[row])
            if row % 10000 == 0:
                print row
        #Redo the centroids
        copyroids = centroids.copy()
        for i in range(clusters):
            if len(numlist[i]) > 0:
                centroids[i].put(range(27), np.average(numlist[i], axis=0).astype(np.int32))
        attempt += 1
        if np.any(centroids-copyroids) == 0:
            stop = True
    score(numlist, centroids)
    np.save("Results/clusterdata.npy", numlist)

'''
Performs the K-Means clustering algorithm that Scikit-Learn's cluster package provides.
Saves the output into a file called clusterdata.npy.  This file is located in the Results folder.
'''
def KMeans(filename, clusters, iter):
    data = np.load(filename)
    t0 = time.time()
    estimator = cluster.KMeans(n_clusters=clusters, n_init = 5, max_iter=iter, verbose=1, n_jobs=5)
    estimator.fit(data)
    print('%.2fs    %i'
          % ((time.time() - t0), estimator.inertia_))
    saveddata = [estimator.cluster_centers_, estimator.labels_, estimator.inertia_]
    np.save("Results/clusterdata.npy", saveddata)
