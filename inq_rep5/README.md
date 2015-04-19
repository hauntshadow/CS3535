#Problem
We want to see how to use a K-Means algorithm to compare clusters of segments in the database.

#Questions
1. What is the K-Means algorithm?
2. How can it be used to decrease the time it takes to compare segments?
3. Is there a K-Means clustering algorithm example already made in Python?

#Resource
1. [K-Means Clustering with Scikit-Learn]
2. [Digit Classification Example]

####Mini-abstract and relevance of the [K-Means Clustering with Scikit-Learn]

This resource is a slideshow presentation that covers what the K-Means algorithm is, as well as its practical uses and
applications.  Sarah Guido, the author of this presentation, shows the basic algorithm of how K-Means works, as detailed below:

1. Choose a k that defines the number of desired clusters and randomly initialize them.
2. Assign every element of a dataset to the closest cluster.
3. Update the centers of those clusters.
4. Repeat until no segments change clusters, or until the max number of iterations occurs.

She also gives an example on how to use the dataset.  Her example uses power consumption to cluster user data.  This is 
similar to how our dataset is set up.  Each row in the power consumption dataset contains 7 values.  While ours contains 27
values, this algorithm is not limited to 2 or 3-dimensional data.  This helps us group like segments together, so that we
only need to check the segments in the same cluster as the one we are comparing it to.
 
 This source eads us to answers for our first two questions: "What is the KMeans algorithm?" and  
 "How can it be used to decrease the time it takes to compare segments?"
 
####Mini-abstract and relevance of the [Digit Classification Example]
 
 This source is a program that David Kale, Scott Shuffler, and I wrote during the summer of 2014.  This program takes
 a dataset full of handwritten digits from the Scikit-Learn library, and uses an implemented K-Means algorithm to 
 seperate the digits into ten clusters, where each cluster should represent a unique digit.  This example
 will give us an example to follow when implementing the K-Means algorithm for segment analysis.
 
 This example is written in Python, so it shows that there is an example of a K-Means implementation written in Python, 
 which is our answer to the third question.

 [K-Means Clustering with Scikit-Learn]: http://www.slideshare.net/SarahGuido/kmeans-clustering-with-scikitlearn
 [Digit Classification Example]: https://github.com/kaledj/sstem_python_stuff/blob/master/digit_classification.py
