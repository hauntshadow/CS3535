import numpy as np
from numpy import random
from sklearn import metrics
from sklearn.cluster import MiniBatchKMeans
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA
import time

def classify(x, size, centroids):
    list = np.zeros(size)
    for i in range(size):
        list[i] = np.sqrt(np.sum((centroids[i] - x) ** 2))
    return np.argmin(list)

def score(list, size):
    data = np.zeros((size, 27))
    count = 0
    for i in list:
        data[count] = i[0]
        count += 1
    print (PCA(n_components=size)).explained_variance_ratio_

def seg_kmeans(filename, size, maxattempts):
    """
    np.random.seed(53)
    data = scale(np.load(filename))
    sams, feats = data.shape
    print data.shape
    print "Doing kmeans on your data..."
    kmeans = MiniBatchKMeans(init = 'k-means++', n_clusters = size, max_iter = 1)
    print "Fitting it to your data..."
    t0 = time.time()
    kmeans.fit(data)
    t1 = time.time()
    print "Acquiring results"
    print t1-t0
    inertias = kmeans.inertia_
    print inertias
    """
    #Initialize everything
    data = np.load(filename)
    data.resize(1000,27)
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
    #score(numlist, size)
    print centroids

