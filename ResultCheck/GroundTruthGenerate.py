import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
import time
from collections import Counter

def truth_generator(filename):
    data = np.load(filename)
    data.resize(100000, 27)
    truths = []
    for i in range(len(data)):
        truths.append([])
    t0 = time.time()
    for i in range(0,100000,10000):
        a = data[i:i+10000,]
        a[:,:12:] *= 10
        a[:,26] *= 100
        for j in range(i,100000,10000):
            b = data[j:j+10000,]
            b[:,:12:] *= 10
            b[:,26] *= 100
            c = seg_distances(a,b)
            for k in range(len(c)):
                for l in range(len(c)):
                    if c[k,l] <= 80:
                        truths[k+i].append(l+j)
            print "Done. Onto the next one..."
    print time.time() - t0
    np.save("Results/groundtruths", truths)

def histo_generator(filename):
    data = np.load(filename)
    labels = data[1]
    counter = Counter()
    for i in labels:
        counter[i] += 1
    if np.amax(len(counter)) / 50 >= 5:
        bins = np.amax(len(counter)) / 50
    else:
        bins = 5
    plt.hist(counter.values(), bins = bins)
    plt.title('Number of members per cluster')
    plt.xlabel('Number of members')
    plt.ylabel('Number of occurrences')
    ticks = range(0, bins)
    #plt.xticks(ticks[0::50])
    plt.gcf().savefig('Results/truthCountHistogram.png')
    plt.close()

def seg_distances(u_, v_=None):
    from scipy.spatial.distance import pdist, cdist, squareform
    from numpy import diag, ones
    if v_ is None:
        d_ = pdist(u_[:, 0:12], 'euclidean')
        d_ += pdist(u_[:, 12:24], 'euclidean')
        d_ += pdist(u_[:, 24:], 'cityblock')
        d_ = squareform(d_) + diag(float('NaN') * ones((u_.shape[0],)))
    else:
        d_ = cdist(u_[:, 0:12], v_[:, 0:12], 'euclidean')
        d_ += cdist(u_[:, 12:24], v_[:, 12:24], 'euclidean')
        d_ += cdist(u_[:, 24:], v_[:, 24:], 'cityblock')

    return d_
