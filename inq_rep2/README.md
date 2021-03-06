#Problem
We want to graph the distances between every pair of segments in a song.

#Questions
1. How do we get the segments from a song?
2. How do we get the data from each segment?
3. How do we graph a list of data?

#Resources
1. [EchoNest Remix API]
2. [Python Counter objects]
3. [Pyplot Histogram Docs]

####Mini-abstract and relevance of the [EchoNest Remix API]
 The [EchoNest Remix API] is the documentation for the module that allows us to extract a song's data.  This data can be obtained from either a song ID or a local audio file.  We are able to get the segments, as well as their data, with the [EchoNest Remix API].  In order to compare the segments, the [Infinite Jukebox] uses each segment's pitch, timbre, starting loudness, max loudness, and its duration.  The following code snippet shows how to get each of these pieces of data for a segment.
 
 The following code shows how to get the tempo from a local song:
 ```python
 import echonest.remix.audio as audio
 #Analyze the song and print the tempo. Output gives confidence and value.
 t = audio.AudioAnalysis("path to the local song")
 segments = t.segments
 pitches = segments.pitches
 timbres = segments.timbre
 loud_maxes = segments.loudness_max
 loud_begins = segments.loudness_begin
 durations = segments.duration
 ```
 However, the duration returns the song's duration.  You must iterate over 
 every segment if you want the individual segment's durations.  This resource
 answers both questions 1 and 2:  "How can we get the segments for a song?  How can 
 we get each segment's data?"
 
 
####Mini-abstract and relevance of [Python Counter objects]

Python has a collections module that is used for various purposes.  One of
the classes in this module is the Counter class.  This class is used for
totalling up the number of occurances of each item in a collection of data.
The dataset must be iterable to be used with Counter.  There are many methods
that can be used with a Counter, including, but not limited to, methods that:
```python
-Get the "n" most common elements
-Listing each element that has at least 1 occurance
-Listing unique elements
-Totalling the elements in the Counter
```

The following code demonstrates how to use the Counter object in Python:
 
 ```python
 from collections import Counter
 a = [1, 3, 3, 3, 4, 4, 6, 8, 17, 20000]
 count = Counter()
 for num in a:
     count[num] += 1
 print count
 ```
 This code prints out the number of occurances of each different number
 in the "a" array.  The order goes from most occurances to fewest occurances.
 This allows us to get the counts for the ranges of data that we need to graph.
 
####Mini-abstract and relevance of [Pyplot Histogram Docs]
 
This documentation talks about how to create a histogram from an array of data.
The pyplot module is inside of the matplotlib package.  Inside of this module is a
function called hist(x).  This function creates a histogram using an array of values, being the "x" array.
Optional inputs include the number of bins for the histogram, the ranges of the bins, and any
potential weights that you want for the bins.

The following example will create a simple histogram from values in the "x" array:
```python
import numpy as np
import matplotlib.pyplot as plt

x=[10, 20, 30, 40, 50, 60, 60, 70, 80, 90]

n = plt.hist(x,9)
plt.show()
```

 [EchoNest Remix API]: http://echonest.github.io/remix/apidocs/
 [Python Counter objects]: https://docs.python.org/3/library/collections.html#counter-objects
 [Infinite Jukebox]: http://labs.echonest.com/Uploader/index.html
 [Pyplot Histogram Docs]: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.hist 
