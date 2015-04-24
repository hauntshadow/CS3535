# res_mod5

This program is designed to take an array of song segment data, and run a K-Means clustering algorithm on the dataset.  Each segment consists of :

1. 12 Numbers for pitch
2. 12 Numbers for timbre
3. 1 Number for the starting loudness
4. 1 Number for the maximum loudness
5. 1 Number for the duration

This program is designed to cluster datasets using the K-Means clustering algorithm provided by [Scikit-Learn].  The parameters of this program are as follows:

1. The filename of the pickled dataset
2. The number of clusters desired
3. The maximum number of iterations for this clustering

There are two methods that can be called in order to cluster the data.  The seg_kmeans function takes all three parameters, and clusters the data once.  The KMeans function does the same thing 5 times, using scikit-learn's functions.

**NOTE: This program needs a pickled numpy array of data to work.  An example of this was done in the h5_array directory.

###What This Program is Useful For

This program is useful for clustering datasets.  This program calls [Scikit-Learn]'s K-Means class in order to run the clustering algorithm with the fastest time.  K-Means allows you to group big datasets together quickly and somewhat efficiently.  This program also uses the multi-threading option for [Scikit-learn]'s K-Means class.  This increases efficientcy of finding the best clustering results.

###The Inspiration Behind This Program

The main inspiration of this program is trying to reduce the time it takes to compare a segment with every other segment in a database.  By doing this algorithm, we can essentially rule out any segment comparisons that involve a segment that is not in the same cluster as the first segment.  This rules out the majority of the database.  For example, if we have 10000 clusters, we can approximately rule out 9999/10000 of the database, as the two segments in question would not be in the same cluster.

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

[1] scikit-learn KMeans Class API: http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

[2] SSTEM Digit Classification Extension: https://github.com/kaledj/sstem_python_stuff/blob/master/digit_classification.py

###Package Dependencies

Using seg_kmeans.py requires these packages:

1. [Python time]
2. [Numpy]
3. [SciPy]
4. [Matplotlib]
5. [Scikit-Learn]

###Example Use

To use this program (assuming you have the previously mentioned packages), you can do
the following to run the seg_kmeans package of code (assuming you have a pickled array of segment data):

```python
import seg_kmeans as s
#Run the non-scikit learn version
a = s.seg_kmeans("Path to the pickled array of data", number of clusters, number of iterations)
#Run the scikit learn version
a = s.KMeans("Path to the pickled array of data", number of clusters, number of iterations)
```

[Numpy]: https://pypi.python.org/pypi/numpy#downloads

[Matplotlib]: http://matplotlib.org/index.html

[Python time]: https://docs.python.org/2/library/time.html

[SciPy]: http://www.scipy.org/

[Scikit-Learn]: http://scikit-learn.org/stable/
