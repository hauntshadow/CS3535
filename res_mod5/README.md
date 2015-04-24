# res_mod5

This program is designed to take an array of song segment data, and run a K-Means clustering algorithm on the dataset.  Each segment consists of :

1. 12 Numbers for pitch
2. 12 Numbers for timbre
3. 1 Number for the starting loudness
4. 1 Number for the maximum loudness
5. 1 Number for the duration

This program is designed to cluster datasets using the K-Means clustering algorithm provided by [Scikit-Learn].  The
parameters of this program are as follows:

1. The filename of the pickled dataset
2. The number of clusters desired
3. The maximum number of iterations for this clustering

There are two methods that can be called in order to cluster the data.  The seg_kmeans function takes all three parameters,
and clusters the data once.  The KMeans function does the same thing 5 times, using scikit-learn's functions.

***NOTE: This program needs a pickled numpy array of data to work.  An example of this was done in the h5_array directory.*

***NOTE: This program also needs a Results directory where the seg_kmeans.py file is.  This allows histograms and clustering 
results to save there.*

###What This Program is Useful For

This program is useful for clustering datasets.  This program calls [Scikit-Learn]'s K-Means class in order to run the
clustering algorithm with the fastest time.  K-Means allows you to group big datasets together quickly and somewhat
efficiently.  This program also uses the multi-threading option for [Scikit-learn]'s K-Means class.  This increases
efficientcy of finding the best clustering results.

###The Inspiration Behind This Program

The main inspiration of this program is trying to reduce the time it takes to compare a segment with every other segment in a
database.  By doing this algorithm, we can essentially rule out any segment comparisons that involve a segment that is not in
the same cluster as the first segment.  This rules out the majority of the database.  For example, if we have 10000 clusters,
we can approximately rule out 9999/10000 of the database, as the two segments in question would not be in the same cluster.

###Code Explanation

The seg_kmeans(filename, clusters, maxattempts) function is a function that takes a pickled array of segment data, and runs a
K-Means clustering algorithm on it.  This K-Means algorithm collectively seperates the data into a defined number of clusters
(labeled as the clusters parameter).  It will continue to try to cluster data and update the center points in those clusters
for a predetermined number of iterations (defined as the maxattempts parameter).  This code computes the distance from a
segment to each center point, and then appends the segment to the list of the closest center point, as seen below [1]:

```python
    for row in range(len(data)):
        closest = classify(data[row], size, centroids)
        numlist[closest].append(data[row])
```

By doing this, we can put every similar segment into a list (which represents a cluster).  After doing this, we copy the
center points, and compute the new centers for the clustered results.  If the center points do not change, then we stop, as
the dataset has converged.  Else, we continue to do this until it either converges, or it reaches the iteration limit. The
following code shows how we determine whether or not the data has converged [1]:

```python
    #Redo the centroids
    copyroids = centroids.copy()
    for i in range(size):
        if len(numlist[i]) > 0:
            centroids[i].put(range(27), np.average(numlist[i], axis=0).astype(np.int32))
    attempt += 1
    if np.any(centroids-copyroids) == 0:
        stop = True
```

After the dataset has converged or reached its iteration limit, we can compute the score of how well it did.  This is done by
looking to see how similar the clusters are in size, as well as the maximum distance from the center point inside of each
cluster.  This is done by the following code:

```python
def score(centers, centroids):
    counts = np.zeros(len(centers))
    maxes = np.zeros(len(centers))
    index = 0
    np.asarray(centers)
    for i in range(len(centers)):
        counts[index] = len(centers[index])
        index += 1
    for i in range(len(centers)):
        maxes[i] = distance.cdist(centers[i], np.asarray(centroids[i]).reshape((1,27)), 'euclidean').max()
```

In this case, the "centers" are the lists of segments pertaining to each center point, while the "centroids" are the actual
center points themselves.  After doing this, we create and save histograms of the cluster sizes and max distance in each
cluster into a Results directory.

The KMeans(filename, clusters, iter) function is a function that simply calls the KMeans class in [Scikit-Learn].  The
data is loaded from the file, then the time is taken using [Python time]'s time() function.  Then, [Scikit-Learn]'s KMeans
class is called (located in the cluster package).  We use "clusters" and "iter" for the number of clusters and iterations
respectively, but we also have verbose mode turned on and max CPU usage turned on [2].  Verbose mode allows us to see the
iteration results, while the max CPU usage allows the data to get fit to the algorithm quicker.  We also limit the number of
different seeds to 5, as this means that the algorithm is ran 5 times with 5 different results.  Then, the best results are
taken [2].  We also print out how long it took, as well as the final inertia of the dataset.  Then, we save the cluster
centers, labels that describe which segments are in which clusters, and the final inertia into a file called
"clusterdata.npy" that is located in the Results directory.

The following code shows how the KMeans(filename, clusters, iter) function is set up:

```python
def KMeans(filename, clusters, iter):
    data = np.load(filename)
    data.resize(1000000, 27)
    t0 = time.time()
    estimator = cluster.KMeans(n_clusters=clusters, max_iter=iter, verbose=1, n_jobs=-1)
    estimator.fit(data)
    print('%.2fs    %i'
          % ((time.time() - t0), estimator.inertia_))
    saveddata = [estimator.cluster_centers_, estimator.labels_, estimator.inertia_]
    np.save("Results/clusterdata.npy", saveddata)
```

###References

The following are links to the information that I found useful in constructing this module:

[1] SSTEM Digit Classification Extension: https://github.com/kaledj/sstem_python_stuff/blob/master/digit_classification.py

[2] scikit-learn KMeans Class API: http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

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
