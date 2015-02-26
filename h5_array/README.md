# h5_seg_to_array

This program takes every segment in the passed in directory (and all of its subdirectories),
and returns an array that contains every segment's features. These features are:

1. 12 Numbers for pitch
2. 12 Numbers for timbre
3. 1 Number for the starting loudness
4. 1 Number for the maximum loudness
5. 1 Number for the duration

###What This Program is Useful For

This program is useful if you want to take a directory (or directories) full of .h5 files, and find
out information about their segments.  Specifically, this program gets information about a segment's
pitch, timbre, max loudness, starting loudness, and duration.  This could be used to find segment
distance, similarly to the [Infinite Jukebox].

###The Inspiration Behind This Program

The inspiration behind this program came from the [Million Song Dataset] and Dr. Parry.  The [Million Song Dataset]
has a million songs in it, and they're all stored in .h5 files.  However, there is no good way to
get the segment data that is in these .h5 files.  This program takes a directory, searches itself and
all subdirectories for .h5 files, and then stores segment information pertaining to pitch, timbre, loudness max, 
starting loudness, and duration.  This information is used to calculate distance between parameters in the
[Infinite Jukebox], so Dr. Parry and I figured having code to generate this information, as well as store and load it, would
be helpful.

###Code Explanation

The h5_files_to_np_array(dir, filename) function is the function that gets the segments and stores the data.
The function starts off by calling get_h5_files(dir) to get the list of .h5 files that are in the directory 'dir',
or any subdirectories.  Then, we set the counter to 0, which counts the number of files parsed, and initialize
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

We open the file, then put pitch values in a new array (indices 0-11), timbre values in 12-23, max loudness
in index 24, and starting loudness in index 25.  However, [hdf5_getters] does not have a function that returns the
segments' durations.  Therefore, we must get the starting times for each segment, and if it's not the last segment, make
the segment's duration equal to the next segment's start time minus the current segment's start time.  Then, the final
segment has its value set to the duration of the song minus the segment's start time.

Then, we put each segment duration at index 26, and extend the list to include the new segments' data that were just created.
We then close the current song, increase the counter by 1, and repeat that whole process for each .h5 file in the list.  Every 500th .h5 file parsed results in printing a statement saying that the number of files parsed is num_dome out of len(list).

After the list is completed, we convert the list into a [Numpy] array, and dump that array into a file called 'filename' (the parameter passed in).  We print the number of segments in the array, and return the array.

There is also an open function that takes a filename as a parameter.  This function calls [Numpy].load on the filename, and returns the [Numpy] array that the load function returns.

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

###References

The following are links to the information that I found useful in constructing this module:

1. [Numpy Documentation] - This documentation helped to understand the available functions in Numpy.
2. [Million Song Dataset] - This documentation helped to understand the format and available functions for the Million Song Dataset.
3. [Infinite Jukebox] - This resource compares segments of songs with a given formula.  This formula was a basis for the extracted data to be stored in the array.
4. [Stack Overflow] - This resource helped my understanding of how to access a file by the full path in Python.

[Numpy]: https://pypi.python.org/pypi/numpy#downloads

[hdf5_getters]: https://github.com/tbertinmahieux/MSongsDB/blob/master/PythonSrc/hdf5_getters.py

[Infinite Jukebox]: http://labs.echonest.com/Uploader/index.html

[Million Song Dataset]: http://labrosa.ee.columbia.edu/millionsong/

[Numpy Documentation]: http://docs.scipy.org/doc/numpy/genindex.html

[Stack Overflow]: http://stackoverflow.com/questions/17730173/python-cant-get-full-path-name-of-file
