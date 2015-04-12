"""
timing.py

Usage: In the functions following this, the parameters are described as follows:

filename: the file that contains segment data

This file must have been a NumPy array of segment data that was saved.  It is loaded through NumPy's load function.

Each segment array is in the following format:

[12 values for segment pitch, 12 values for segment timbre, 1 value for loudness
max, 1 value for loudness start, and 1 value for the segment duration]

Author: Chris Smith

Date: 04.11.2015
"""

import time
import scipy.spatial.distance as distance
import numpy as np

'''
Method that takes a file of segment data (a 2D NumPy array), and compares the first 850 segments to 1000, 10000, 100000, and
1000000 segments.  The results are ignored, as this function times the comparisons.
'''
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
