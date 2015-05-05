import numpy as np

def check(filename):
    clusters = np.load(filename)
    clusters = clusters[1]
    truths = np.load("Results/groundtruths.npy")
    error = 0
    total = 0
    for i in range(len(truths)):
        for j in range(len(truths[i])):
            if clusters[truths[i][j]] != clusters[i]:
                error += 1
            total += 1
    print error
    print total
