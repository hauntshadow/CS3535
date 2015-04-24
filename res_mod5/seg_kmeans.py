import matplotlib
matplotlib.use("Agg")
import numpy as np
from numpy import random
import scipy.spatial.distance as distance
from sklearn import metrics
from sklearn import cluster
import matplotlib.pyplot as plt
import time

def classify(x, size, centroids):
    list = np.zeros(size)
    for i in range(size):
        list[i] = np.sqrt(np.sum((centroids[i] - x) ** 2))
    return np.argmin(list)

def score(centers, centroids):
    counts = np.zeros(len(centers))
    #centroids = np.zeros(len(centers))
    maxes = np.zeros(len(centers))
    index = 0
    np.asarray(centers)
    for i in range(len(centers)):
        #np.asarray(centers[i])
        #for j in range(len(centers[i])):
        #    np.asarray(centers[i][j])
        counts[index] = len(centers[index])
        index += 1
    for i in range(len(centers)):
        maxes[i] = distance.cdist(centers[i], np.asarray(centroids[i]).reshape((1,27)), 'euclidean').max()
    plt.hist(counts.ravel(), bins = np.amax(counts) / 50)
    plt.title('Number of members per cluster')
    plt.xlabel('Number of members')
    plt.ylabel('Number of occurrences')
    ticks = range(0, int(np.amax(counts)))
    plt.xticks(ticks[0::50])
    plt.gcf().savefig('Results/countHistogram.png')
    plt.close()
    plt.hist(maxes.ravel(), bins = np.amax(maxes) / 50)
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

def seg_kmeans(filename, size, maxattempts):
    #Initialize everything
    data = np.load(filename)
    data.resize(10000,27)
    centroids = np.empty((size, 27))
    copyroids = np.empty((size, 27))
    for i in range(0, size):
        sample = random.randint(0, len(data))
        centroids[i] = data[sample]
    #Start the algorithm
    stop = False
    attempt = 1
    numlist = []
    while not stop and attempt <= maxattempts :
        #Initialize the lists
        numlist = []
        for i in range(size):
            numlist.append([])
        print "Attempt Number: %d" % attempt
        #Classify stuff
        for row in range(len(data)):
            closest = classify(data[row], size, centroids)
            numlist[closest].append(data[row])
            if row % 10000 == 0:
                print row
        #Redo the centroids
        copyroids = centroids.copy()
        for i in range(size):
            if len(numlist[i]) > 0:
                centroids[i].put(range(27), np.average(numlist[i], axis=0).astype(np.int32))
        attempt += 1
        if np.any(centroids-copyroids) == 0:
            stop = True
    score(numlist, centroids)

def KMeans(filename, clusters, iter):
    data = np.load(filename)
    data.resize(1000000, 27)
    t0 = time.time()
    estimator = cluster.KMeans(n_clusters=clusters, max_iter=iter, verbose=1, n_jobs=-1)
    estimator.fit(data)
    print('%.2fs    %i'
          % ((time.time() - t0), estimator.inertia_))
    saveddata = [estimator.cluster_centers_, estimator.labels_, estimator.inertia_]
    np.save("Results/clusterdata.npy", saveddata)
