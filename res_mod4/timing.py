import time
import scipy.spatial.distance as distance
import numpy as np

def comp_time(filename):
    seg_array = np.load(filename)
    song = seg_array[:850:].copy()
    t1 = time.time()
    distance.cdist(song, seg_array[:1000:],'euclidean')
    t2 = time.time()
    distance.cdist(song, seg_array[:10000:],'euclidean')
    t3 = time.time()
    distance.cdist(song, seg_array[:100000:],'euclidean')
    t4 = time.time()
    distance.cdist(song, seg_array[:1000000:],'euclidean')
    t5 = time.time()
    print "Time for comparisons between a song and 1000 segments: " + str(t2-t1)
    print "Time for comparisons between a song and 10000 segments: " + str(t3-t2)
    print "Time for comparisons between a song and 100000 segments: " + str(t4-t3)
    print "Time for comparisons between a song and 1000000 segments: " + str(t5-t4)
