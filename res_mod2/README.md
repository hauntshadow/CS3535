# res_mod2

This program takes a song, and compares every segment inside the song to every other segment. Each
segment consists of :

1. 12 Numbers for pitch
2. 12 Numbers for timbre
3. 1 Number for the starting loudness
4. 1 Number for the maximum loudness
5. 1 Number for the duration

These features are calculated, added together, and checked to see whether or not the distance between the two segments is below a certain threshold (45 for this program).  Then, the distances are graphed into a histogram, and the percentage below 45 is calculated.

###What This Program is Useful For

This program is useful if you want to find out how self-similar a song is to itself.  This program compares segments inside the song similarly to the [Infinite Jukebox], as this program uses the same information, as well as the same weights.  However, this program will give you a percentage of distances that are below 45, as well as the percentage of segments who have at least 1 other segment that is at most 45 away from it.  Plus, this program produces a histogram of the distances, and gives you no graphic displaying which segments are similar.

###The Inspiration Behind This Program

The [Infinite Jukebox] was the main inspiration behind this program.  The [Infinite Jukebox] uses 27 numbers to calculate the distance between 2 segments.  It also applies weights to these numbers to tune the comparisons to human perception.  This program uses the same numbers and the same weights, but instead calculates the percentage of the segments that are similar to another segment inside the song.  It also calculates the percentage of two-segment combinations that have a distance of at most 45.  This is a gauge for how repetitive a song is.

###Code Explanation

The self_seg_compare() function is a function that takes a song (via Track ID), computes the differences between every pair of segments that are not the same segment, generates a histogram of the differences, and returns the adjacency list of the segments.  The differences are calculated from the [Infinite Jukebox]'s method of calculating differences [1].  The following is a snippet of code that shows how the segment data is obtaine, as well as how the segment differences are calculated:

```python
    audiofile = audio.AudioAnalysis(track_id)
    segments = audiofile.segments
    #Get each segment's array of comparison data
    segs = np.array(segments.pitches)
    segs = np.c_[segs, np.array(segments.timbre)]
    segs = np.c_[segs, np.array(segments.loudness_max)]
    segs = np.c_[segs, np.array(segments.loudness_begin)]
    segs = np.c_[segs, np.ones(len(segs))]
    ...
    #Finish getting the comparison data
    for i in range(len(segs)):
        segs[i][26] = segments[i].duration
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
            distances[i][j] = distances[i][j] + abs(segs[i][25] - segs[j][25]) + abs(segs[i][26] - segs[j][26]) * 100
```

The segments' pitches are converted into an array.  Then, the timbre arrays are added onto the end of the rows.  Afterwards, the maximum loudness, beginning loudness, and a column of 1s are added on.  The column of ones are then changed to each segment's duration.

The euclidean distances are found from the first 12 columns of every pair of possible segments (the pitches), and then multiplied by 10, as the [Infinite Jukebox] does [1].  The distance for every pair of segments obtained this way is added to the euclidean distance from columns 13-24, plus the differences in the max loudness, starting loudness, and durations * 100 [1].

Afterwards, we get the adjacency list by seeing if the difference between any two segments is at most 45.  Then, we do the following code to get a histogram of the distances:

```python
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
    #Make each tick on the y-axis correspond to each 25000th number up to the number of possible tuple combos / 2.
    plt.yticks(range(0, (len(segments) ** 2 - len(segments))/2 + 25000, 25000))
    plt.gcf().savefig('sim_histogram.png')
```

This portion of the code gets the number of bins by dividing the maximum value inside of the distances 2D array by the threshold, whose default is 45.  In order to plot every combination on one axis, the array must be raveled, which returns a flattened (one-dimensional) [NumPy] array [2].  The title of the histogram, as well as axis labels are put onto the histogram.  Then, in order to show how much of the distances are less than the threshold, a red, dashed, vertical line is plotted [3].  The tick marks on the x and y axes are then modified to the threshold and the potential combinations * 25000 respectively [4].  Finally, the current figure is saved into a file called 'sim_histogram.png' [3].

###References

The following are links to the information that I found useful in constructing this module:

[1] Infinite Jukebox: http://labs.echonest.com/Uploader/index.html

[2] Numpy Ravel: http://docs.scipy.org/doc/numpy/reference/generated/numpy.ravel.html

[3] Pyplot API: http://matplotlib.org/api/pyplot_api.html

[4] Stack Overflow: http://stackoverflow.com/questions/12608788/changing-the-tick-frequency-on-x-or-y-axis-in-matplotlib

###Package Dependencies

Using self_compare_dist.py requires these packages:

1. [EchoNest.Remix]
2. [Numpy]
3. [Matplotlib]
4. [SciPy]

###Example Use

To use this program (assuming you have the previously mentioned packages), you can do
the following to get the adjacency list of a song and save a histogram of the differences:

```python
import self_compare_dist.py as comp
#Compare every pair of segments, save a histogram of the differences, and return the adjacency list
a = comp.self_seg_compare()
#Print out the segment indices who are within a distance of 45 to the second segment.
print a[1]
```

[Numpy]: https://pypi.python.org/pypi/numpy#downloads

[EchoNest.Remix]: http://echonest.github.io/remix/apidocs/

[Infinite Jukebox]: http://labs.echonest.com/Uploader/index.html

[Matplotlib]: http://matplotlib.org/contents.html

[SciPy]: http://matplotlib.org/index.html
