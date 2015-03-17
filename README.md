# CS3535
Music Informatics

##h5_array
This code takes a directory and searches itself and all subdirectories for .h5 files, and puts them into a list.
Then, the code takes every segment from every file and gets the pitches, timbres, loudnesses, and duration of each segment.
That data gets added to the end of a list as a Numpy array.  Then, that list gets converted to a Numpy array.
The array is pickled and saved into a file, then the array is returned.  The ending array has the dimensions:

(number of segments, 27)

##inq_rep1
This is a short report pertaining to the use of EyeD3 to get the information from a local .mp3 file's ID# tags.

##inq_rep2
Coming soon...

##mylimp
This code simply takes the limp example from EchoNest's examples, and changes it so that
each beat has the last tatum taken out of it.  The original EchoNest example had the last
beat (or group of tatums) taken out of each bar.
##one_segment
This code simply takes each bar and gets the first segment out of each bar in a song. This
code was also an EchoNest example.  However, this code was modified to get the first segment
out of each bar, instead of retrieving the first beat out of each bar.
##res_mod2
This code takes a song (received by the EchoNest track id), and gets an adjacency list for every segment.
An adjacency list for a segment represents the segments that are within a certain distance (threshold) from 
that segment.  The code also saves a histogram of the distances between every pair of segments.
