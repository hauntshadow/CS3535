"""
dir_comp.py

Usage: In the functions following this, the parameters are described as follows:

dir: the directory to search

Program that parses all .mp3 files in the passed in directory,
gets the segment arrays from each .mp3 file and puts them into a
numpy array for later use.  Each segment array is in the following format:

[12 values for segment pitch, 12 values for segment timbre, 1 value for loudness
max, 1 value for loudness start, and 1 value for the segment duration]

Author: Chris Smith

Date: 03.27.2015
"""
import matplotlib
matplotlib.use("Agg")
import pyechonest
import echonest.remix.audio as audio
import matplotlib.pyplot as plt
import scipy.spatial.distance as distance
import os
import numpy as np

'''
Method that takes a directory, searches that directory, and returns a list of every .mp3 file in it.
'''
def get_mp3_files(dir):
    list = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            name, extension = os.path.splitext(file)
            if extension == ".mp3":
                list.append(os.path.realpath(os.path.join(root, file)))
    return list

'''
Method that takes two .mp3 files and compares every segment within song A to 
every segment in song B and supplies a histogram that shows
the distances between segments (tuples of segments).  Also supplies some data
about the songs that were parsed.
'''
def two_song_comp(fileA, fileB):
    #Defines the threshold for comparisons
    thres = 45
    nameA = os.path.basename(os.path.splitext(fileA)[0])
    nameB = os.path.basename(os.path.splitext(fileB)[0])
    adj_listA = []
    adj_listB = []
    sim_seg_countA = 0
    sim_seg_countB = 0
    sim_countA = 0
    sim_countB = 0
    audiofileA = audio.AudioAnalysis(fileA)
    audiofileB = audio.AudioAnalysis(fileB)
    segmentsA = audiofileA.segments
    segmentsB = audiofileB.segments
    #Get each segment's array of comparison data for song A
    segsA = np.array(segmentsA.pitches)
    segsA = np.c_[segsA, np.array(segmentsA.timbre)]
    segsA = np.c_[segsA, np.array(segmentsA.loudness_max)]
    segsA = np.c_[segsA, np.array(segmentsA.loudness_begin)]
    segsA = np.c_[segsA, np.ones(len(segsA))]
    #Get each segment's array of comparison data for song B
    segsB = np.array(segmentsB.pitches)
    segsB = np.c_[segsB, np.array(segmentsB.timbre)]
    segsB = np.c_[segsB, np.array(segmentsB.loudness_max)]
    segsB = np.c_[segsB, np.array(segmentsB.loudness_begin)]
    segsB = np.c_[segsB, np.ones(len(segsB))]

    #Finish creating the adjacency list
    for i in segmentsA:
        adj_listA.append([])
    for i in segmentsB:
        adj_listB.append([])
    #Finish getting the comparison data
    for i in range(len(segsA)):
        segsA[i][26] = segmentsA[i].duration
    for i in range(len(segsB)):
        segsB[i][26] = segmentsB[i].duration
    #Get the euclidean distance for the pitch vectors, then multiply by 10
    distances = distance.cdist(segsA[:,:12], segsB[:,:12], 'euclidean')
    for i in range(len(distances)):
        for j in range(len(distances[i])):
            distances[i][j] = 10 * distances[i][j]
    #Get the euclidean distance for the timbre vectors, adding it to the
    #pitch distance
    distances = distances + distance.cdist(segsA[:,12:24], segsB[:,12:24], 'euclidean')
    #Get the rest of the distance calculations, adding them to the previous
    #calculations.
    for i in range(len(distances)):
        for j in range(len(distances[i])):
            distances[i][j] = distances[i][j] + abs(segsA[i][24] - segsB[j][24])
            distances[i][j] = distances[i][j] + abs(segsA[i][25] - segsB[j][25]) + abs(segsA[i][26] - segsB[j][26]) * 100
    i_point = 0
    j_point = 0
    #Use i_point and j_point for the indices in the 2D distances array
    for i_point in range(len(distances)):
        for j_point in range(len(distances[i])):
            #Check to see if the distance between segment # i_point and
            #segment # j_point is less than 45
            if abs(distances[i_point][j_point]) <= thres:
                #Add to the adjacency lists if not already there
                if j_point not in adj_listA[i_point]:
                    adj_listA[i_point].append(j_point)
                if i_point not in adj_listB[j_point]:
                    adj_listB[j_point].append(i_point)
            j_point = j_point + 1
        i_point = i_point + 1
        j_point = 0
    #Get the count of the similarities in the adjacency lists
    for i in adj_listA:
        if len(i) > 0:
            sim_countA = sim_countA + len(i);
            sim_seg_countA = sim_seg_countA + 1
    for i in adj_listB:
        if len(i) > 0:
            sim_countB = sim_countB + len(i);
            sim_seg_countB = sim_seg_countB + 1

            #print i, "\n"
    print "Num of segments with at least 1 match in song A: ", sim_seg_countA, " out of", len(segmentsA)
    print "Percentage of segments with at least 1 match in song A: ", (sim_seg_countA / float(len(segmentsA)) * 100), "%"
    print "Num of similar tuples: ", sim_countA, " out of ", len(segmentsA) *len(segmentsB)
    print "Percentage of possible tuples that are similar: ", sim_countA / float(len(segmentsA) * len(segmentsB)) * 100, "%"
    print "Num of segments with at least 1 match in song B: ", sim_seg_countB, " out of", len(segmentsB)
    print "Percentage of segments with at least 1 match in song B: ", (sim_seg_countB / float(len(segmentsB)) * 100), "%"
    #Get the number of bins.  Calculated by taking the max range and dividing by 50
    bins = int(np.amax(distances)) / thres
    #Make the histogram with titles and axis labels.  Plot the line x=thres for visual comparison.
    plt.hist(distances.ravel(), bins = bins)
    plt.title('Distances between Tuples of Segments' + nameA + nameB)
    plt.xlabel('Distances')
    plt.ylabel('Number of occurrences')
    plt.axvline(thres, color = 'r', linestyle = 'dashed')
    #Make each tick on the x-axis correspond to the end of a bin.
    plt.xticks(range(0, int(np.amax(distances) + 2 * thres), thres))
    #Make each tick on the y-axis correspond to each 25000th number up to the number of possible tuple combos / 2.
    plt.yticks(range(0, (len(segmentsA) * len(segmentsB))/2 + 25000, 25000))
    plt.gcf().savefig('Histograms/' + nameA + 'and' + nameB + '_histogram.png')
    plt.close()

'''
Method that runs the comparison on every pair of .mp3 files in a directory
'''
def dir_comp(dir):
    files = get_mp3_files(dir)
    for f1 in files:
        for f2 in files:
            nameA = os.path.basename(os.path.splitext(f1)[0])
            nameB = os.path.basename(os.path.splitext(f2)[0])
            if not os.path.isfile('Histograms/' + nameA + 'and' + nameB + '_histogram.png') and not os.path.isfile('Histograms/' + nameB + 'and' + nameA + '_histogram.png'):
                two_song_comp(f1, f2)
                print "Comparison completed!"
    print "Finished."
