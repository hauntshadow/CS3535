#Problem
We want to see how long it takes for a song to get compared to a group of segments.

#Questions
1. How do we find out the amount of time it took for one segment to get compared to another?
2. How do we find the amount of time it took for a group of segments to get compared to a song?
3. How do we use K-Means Clustering in Python?

#Resource
1. [Python Time API]
2. [Scikit Learn Clustering API]

####Mini-abstract and relevance of the [Python Time API]
 The [Python Time API] is the documentation for the module that allows us to get the current time.  This module has a function 
 called time() that returns the value in seconds since January 1st, 1970.  This is useful, since you can calculate the amount
 of time something takes to run by doing the following:
 
 ```python
 import time
 start = time.time()
 #Do whatever you want to time
 stop = time.time()
 print stop-start
 ```
 
 This essentially answers the first two questions that we have: "How long would it take to compare one segment to another? 
 What about comparing one song to a group of segments?"
 
 ####Mini-abstract and relevance of the [Scikit Learn Clustering API]
 
 This source is Scikit Learn's answer to our question 3: "How do we use K-Means Clustering in Python?"
 By importing sklearn.cluster, you have access to many algorithms, including the K-Means clustering algorithm.
 You can use many different parameters, including the number of clusters, the number of iterations, and how the algorithm
 is initialized.  This is really important, especially when it comes to the accuracy of the clusters' final positions.  This
 will eventually let us compare a database of segments much faster than checking every one, since you'll only compare those
 that are in the same cluster.

 [Python Time API]: https://docs.python.org/2/library/time.html
 [Scikit Learn Clustering API]: http://scikit-learn.org/stable/modules/clustering.html
