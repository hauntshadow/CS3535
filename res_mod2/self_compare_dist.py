#
# Self_compare_dist.py
# Takes the segments of a song, compares them using the Infinite Jukebox's
# fields and weights, and gives a percentage of segments that have another
# segment within 45 of itself.  It also saves a histogram of these
# distances.  The histogram only shows distances <= 800, and up to 600
# matches in each bin.
# Created by: Chris Smith
# Date: 3.11.2015
#
#

import matplotlib
matplotlib.use("Agg")
import echonest.remix.audio as audio
import matplotlib.pyplot as plt
import scipy.spatial.distance as distance
import numpy as np
def main():
    #Defines the threshold for comparisons
    thres = 45
    adj_list = []
    sim_seg_count = 0
    sim_count = 0
    track_id = "TRAWRYX14B7663BAE0"
    audiofile = audio.AudioAnalysis(track_id)
    segments = audiofile.segments
    #Get each segment's array of comparison data
    segs = np.array(segments.pitches)
    segs = np.c_[segs, np.array(segments.timbre)]
    segs = np.c_[segs, np.array(segments.loudness_max)]
    segs = np.c_[segs, np.array(segments.loudness_begin)]
    segs = np.c_[segs, np.ones(len(segs))]
    #Finish creating the adjacency list
    for i in segments:
        adj_list.append([])
    #Finish getting the comparison data
    for i in range(len(segs)):
        segs[i][26] = 100 * segments[i].duration
    #Get the euclidean distance for the pitch vectors, then multiply by 10
    distances = distance.cdist(segs[:,:12], segs[:,:12], 'euclidean')
    for i in range(len(distances)):
        for j in range(len(distances)):
            distances[i][j] = 10 * distances[i][j]
    #Get the euclidean distance for the timbre vectors, adding it to the
    #pitch distance
    distances = distances + distance.cdist(segs[:,12:24], segs[:,12:24], 'euclidean')
    #Get the rest of the distance calculations, adding them to the previous
    #calculations.
    for i in range(len(distances)):
        for j in range(len(distances)):
            distances[i][j] = distances[i][j] + abs(segs[i][24] - segs[j][24])
            distances[i][j] = distances[i][j] + abs(segs[i][25] - segs[j][25]) + abs(segs[i][26] - segs[j][26])
    i_point = 0
    j_point = 0
    #Use i_point and j_point for the indices in the 2D distances array
    for i_point in range(len(distances)):
        for j_point in range(len(distances)):
            if i_point != j_point:
                #Check to see if the distance between segment # i_point and
                #segment # j_point is less than 45
                if abs(distances[i_point][j_point]) <= thres:
                    #Add to the adjacency lists if not already there
                    if j_point not in adj_list[i_point]:
                        adj_list[i_point].append(j_point)
                    if i_point not in adj_list[j_point]:
                        adj_list[j_point].append(i_point)
            j_point = j_point + 1
        i_point = i_point + 1
        j_point = 0
    #Get the count of the similarities in the adjacency lists
    for i in adj_list:
        if len(i) > 0:
            sim_count = sim_count + len(i);
            sim_seg_count = sim_seg_count + 1
            #print i, "\n"
    print "Num of segments with at least 1 match: ", sim_seg_count, " out of", len(segments)
    print "Percentage of segments with at least 1 match: ", (sim_seg_count / float(len(segments)) * 100), "%"
    print "Num of similar tuples: ", sim_count, " out of ", len(segments) ** 2 - len(segments)
    print "Percentage of possible tuples that are similar: ", (sim_count / float(len(segments) ** 2 - len(segments))) * 100, "%"
    print "Note:This takes out comparisons between a segment and itself."
    #Get the number of bins.  Calculated by taking the max range and dividing by 50
    bins = int(np.amax(distances)) / thres
    #Make the histogram with titles and axis labels.  Plot the line x=thres for visual comparison.
    plt.hist(distances.ravel(), bins = bins)
    plt.title('Distances between Tuples of Segments')
    plt.xlabel('Distances')
    plt.ylabel('Number of occurrences')
    plt.axvline(thres, color = 'r', linestyle = 'dashed')
    #Make each tick on the x-axis correspond to the end of a bin.
    plt.xticks(range(0, int(np.amax(distances) + 2 * thres), thres))
    #Make each tick on the y-axis correspond to each 25000th number up to the number of possible tuple combos.
    plt.yticks(range(0, (len(segments) ** 2 - len(segments))/2 + 25000, 25000))
    plt.gcf().savefig('sim_histogram.png')
    return adj_list

