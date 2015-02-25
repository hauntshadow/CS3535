"""
h5_seg_to_array.py

Usage: In the functions following this, the parameters are described as follows:

dir: the directory to search

filename: the filename for saving/loading the results to/from

Program that parses all .h5 files in the passed in directory and subdirectories,
getting the segment arrays from each .h5 file and putting them into a 
numpy array for later use.  Each segment array is in the following format:

[12 values for segment pitch, 12 values for segment timbre, 1 value for loudness
max, 1 value for loudness start, and 1 value for the segment duration]

This program uses the hdf5_getters, which can be found here:
https://github.com/tbertinmahieux/MSongsDB/blob/master/PythonSrc/hdf5_getters.py

Author: Chris Smith

Date: 02.22.2015
"""
import os
import numpy as np
import hdf5_getters as getters

'''
Method that takes a directory, searches that directory, as well as any 
subdirectories, and returns a list of every .h5 file.
'''
def get_h5_files(dir):
    list = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            name, extension = os.path.splitext(file)
            if extension == ".h5":
                list.append(os.path.realpath(os.path.join(root, file)))
        for subdir in dirs:
            get_h5_files(subdir)
    return list

'''
Method that takes a directory, gets every .h5 file in that directory (plus any
subdirectories), and then parses those files.  The outcome is a Numpy array
that contains every segment in each file. Each row in the array of arrays
contains pitch, timbre, loudness max, loudness start, and the duration of each
segment.
''' 
def h5_files_to_np_array(dir, filename):
    list = get_h5_files(dir)
    num_done = 0
    seg_array = []
    #Go through every file and get the desired information.
    for file in list:
        song = getters.open_h5_file_read(file)
        seg_append = np.array(getters.get_segments_pitches(song))
        seg_append = np.c_[ seg_append, np.array(getters.get_segments_timbre(song))]
        seg_append = np.c_[seg_append, np.array(getters.get_segments_loudness_max(song))]
        seg_append = np.c_[seg_append, np.array(getters.get_segments_loudness_start(song))]
        start = np.array(getters.get_segments_start(song))
        for i in range(0,len(start)-1):    
            if i != (len(start) - 1):
                start[i] = start[i+1] - start[i]
        start[len(start) - 1] = getters.get_duration(song) - start[len(start) - 1]
        seg_append = np.c_[seg_append, start]
        #Add the arrays to the bottom of the list
        seg_array.extend(seg_append.tolist())
        song.close()
        num_done = num_done + 1
        #Gives a count for every 500 files completed
        if num_done % 500 == 0:
            print num_done," of ",len(list)
    #Convert the list to a Numpy array
    seg_array = np.array(seg_array)
    #Save the array in a file
    seg_array.dump(filename)
    print len(seg_array)," number of segments in the set."
    return seg_array
    
'''
Method that opens the file with that filename.  The file must contain a 
Numpy array.  This method returns the array.
'''
def open(filename):
    data = np.load(filename)
    return data
