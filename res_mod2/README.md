# h5_seg_to_array

This program takes a song, and compares every segment inside the song to every other segment. Each
segment consists of :

1. 12 Numbers for pitch
2. 12 Numbers for timbre
3. 1 Number for the starting loudness
4. 1 Number for the maximum loudness
5. 1 Number for the duration

These features are calculated, added together, and checked to see whether or not the distance between the two segments is below a certain threshold (80 for this program).  Then, the distances are graphed into a histogram, and the percentage below 80 is calculated.

###What This Program is Useful For

This program is useful if you want to find out how self-similar a song is to itself.  This program compares segments inside the song similarly to the [Infinite Jukebox], as this program uses the same information, as well as the same weights.  However, this program will give you a percentage of distances that are below 80.  Plus, this program produces a histogram of the distances, and gives you no graphic displaying which segments are similar.

###The Inspiration Behind This Program

The [Infinite Jukebox] was the main inspiration behind this program.  The [Infinite Jukebox] uses 27 numbers to calculate the distance between 2 segments.  It also applies weights to these numbers to tune the comparisons to human perception.  This program uses the same numbers and the same weights, but instead calculates the percentage of the segments that are similar to another segment inside the song.  This is a gauge for how repetitive a song is.

###Code Explanation

The h5_files_to_np_array(dir, filename) function is the function that gets the segments and stores the data.
The function starts off by calling get_h5_files(dir) to get the list of .h5 files that are in the directory 'dir',
or any subdirectories [1].  Then, we set the counter to 0, which counts the number of files parsed, and initialize
an empty list for the array of segment data.

Afterwards, we do this code to get the data, create the array for the segment, and append that array to the list:
```python
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
```

We open the file, then put pitch values in a new array (indices 0-11) using get_segments_pitches [2], timbre values in 12-23 using get_segments_timbres [2], max loudness in index 24 using get_segments_loudness_max [2], and starting loudness in index 25 using get_segments_loudness_start [2].  However, [hdf5_getters] does not have a function that returns the
segments' durations.  Therefore, we must get the starting times for each segment using get_segments_start [2], and if it's not the last segment, make the segment's duration (received by using get_duration [2]) equal to the next segment's start time minus the current segment's start time.  Then, the final segment has its value set to the duration of the song minus the segment's start time.

Then, we put each segment duration at index 26, and extend the list to include the new segments' data that were just created.
We then close the current song, increase the counter by 1, and repeat that whole process for each .h5 file in the list.  Every 500th .h5 file parsed results in printing a statement saying that the number of files parsed is num_dome out of len(list).

After the list is completed, we convert the list into a [Numpy] array, and dump a pickle of that array into a file called 'filename' (the parameter passed in) using the dump function [3].  We print the number of segments in the array, and return the array.

There is also an open function that takes a filename as a parameter.  This function calls the load function on the filename [4], and returns the [Numpy] array that the load function returns.

###References

The following are links to the information that I found useful in constructing this module:

[1] Stack Overflow: http://stackoverflow.com/questions/17730173/python-cant-get-full-path-name-of-file

[2] Million Song Dataset: http://labrosa.ee.columbia.edu/millionsong/pages/code

[3] Numpy Dump Function: http://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.dump.html

[4] Numpy Load Function: http://docs.scipy.org/doc/numpy/reference/generated/numpy.load.html#numpy.load
###Package Dependencies

Using h5_seg_to_array.py requires these packages:

1. os (part of Python)
2. [Numpy]
3. [hdf5_getters]

###Example Use

To use this program (assuming you have the previously mentioned packages), you can do
the following to get and save the array in a file:

```python
import h5_seg_to_array as h
#Get the files, generate the array, and store the array in the file
a = h.h5_files_to_np_array("path to the directory with .h5 files in it", "destination filename")
#Print out the second segment in the dataset
print a[1]
```

To load the file, you need to do the following:
```python
import h5_seg_to_array as h
#Load the file into a variable
loadedArray = h.open("filename that holds the numpy array")
#Print out the second segment's duration in the dataset
print loadedArray[1][26]
```


[Numpy]: https://pypi.python.org/pypi/numpy#downloads

[hdf5_getters]: https://github.com/tbertinmahieux/MSongsDB/blob/master/PythonSrc/hdf5_getters.py

[Infinite Jukebox]: http://labs.echonest.com/Uploader/index.html

[Million Song Dataset]: http://labrosa.ee.columbia.edu/millionsong
