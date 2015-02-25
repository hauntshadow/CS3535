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
[Infinite Jukebox], so Dr. Parry and I figured having code to generate this information, as well as store it, would
be helpful.

###Code Explanation



###Package Dependencies

Using h5_seg_to_array.py requires these packages:

1. os (part of Python)
2. [Numpy]
3. [hdf5_getters]

###Example Use



[Numpy]: https://pypi.python.org/pypi/numpy#downloads

[hdf5_getters]: https://github.com/tbertinmahieux/MSongsDB/blob/master/PythonSrc/hdf5_getters.py

[Infinite Jukebox]: http://labs.echonest.com/Uploader/index.html
