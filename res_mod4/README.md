# res_mod4

This program is designed to take an array of song segment data, and time how long it takes to calculate the distance between pairs of segments.  Each segment consists of :

1. 12 Numbers for pitch
2. 12 Numbers for timbre
3. 1 Number for the starting loudness
4. 1 Number for the maximum loudness
5. 1 Number for the duration

This program compares a song of 850 segments to groups of 1000, 10000, 100000, and 1000000 segments.  This allows us to see
whether or not comparing segments is a linear task or not.

**NOTE: This program needs a pickled array of segment data to work.  An example of this was done in the h5_array directory.

###What This Program is Useful For

This program is useful to find out the time constraint for comparing groups of segments (or songs).  Finding out the complexity
of the data can help determine the time costs of a program dealing with song/segment comparisons.

###The Inspiration Behind This Program

The main inspiration of this program is learning the efficiency of programs.  We need to see if the time that it takes
to compare segments can be reduced.  This can dramatically increase the performance of music-based programs that utilize
segment comparisons.

###Code Explanation

The comp_time(filename) function is a function that takes a pickled array of segment data, and computes distances between
the first 850 segments and groups of segments.  The first 850 segments represent the average number of segments in a song, as
per the Million Song Subset, which is a part of the [Million Song Dataset].  Since 850 is the rough average segment count
for a song, we'll consider that to be a song.  Then, the code uses the [Python time] module to calculate time [1].
The following is an example snippet that shows how the [Python time] module is used:

```python
    t1 = time.time()
    distance.cdist(song, seg_array[:1000:],'euclidean')
    t2 = time.time()
    print "Time for comparisons between a song and 1000 segments: " + str(t2-t1)
```

This piece of code simply takes the song (first 850 segments), and compares them to the first 1000 segments using
Euclidean distance and the cdist function [2].  

Then, we do this for the following amounts of segments:
1. 1000 segments
2. 10000 segments
3. 100000 segments
4. 1000000 segments

This allows us to get the amount of time to run each of these specified segment counts.  Then, we can compare them together
to see if the times are linear as predicted.

After running the comp_time function on the array created from the Million Song Subset, I received these values:
<table><tr><td>
Segment count</td><td>Time in seconds</td></tr>
<tr><td>1000</td><td>0.048688</td></tr>
<tr><td>10000</td><td>1.157556</td></tr>
<tr><td>100000</td><td>11.679945</td></tr>
<tr><td>1000000</td><td>163.738721</td></tr></table>

By getting these values, we can divide the number of seconds by 850 to see how long it took for one segment to be compared to
all of the selected segments.

That gives us these values:

<table><tr><td>
Segment count</td><td>Time in seconds</td></tr>
<tr><td>1000</td><td>0.00005728</td></tr>
<tr><td>10000</td><td>0.00136183</td></tr>
<tr><td>100000</td><td>0.01374111</td></tr>
<tr><td>1000000</td><td>0.19263379</td></tr></table>

If segment comparisons are linear, then the times should have their decimal points shifted by one. For example, from 10000 to
100000, if the decimal is shifted to the left by 1 in the 10000 row, then if it is linear, it would nearly equal the 100000
row.  Although the comparison between the 1000 and 10000 rows are not quite linear, the other rows are fairly close to each
other, so the act of comparing groups of segments should be linear.


###References

The following are links to the information that I found useful in constructing this module:

[1] Python Time API: https://docs.python.org/2/library/time.html

[2] Scipy cdist API: http://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cdist.html

###Package Dependencies

Using timing.py requires these packages:

1. [Python time]
2. [Numpy]
3. [SciPy]

###Example Use

To use this program (assuming you have the previously mentioned packages), you can do
the following to run the comp_time code (assuming you have a pickled array of segment data):

```python
import timing as t
#Compare every pair of segments in 2 songs in a directory, save a histogram of the differences, and print statistics
a = t.comp_time("Path to the pickled array of data")
```

[Numpy]: https://pypi.python.org/pypi/numpy#downloads

[Million Song Dataset]: http://labrosa.ee.columbia.edu/millionsong/

[Python time]: https://docs.python.org/2/library/time.html

[SciPy]: http://www.scipy.org/
