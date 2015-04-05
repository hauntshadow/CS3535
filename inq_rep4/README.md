#Problem
We want to see how long it takes for a song to get compared to a group of segments.

#Questions
1. How do we find out the amount of time it took for one segment to get compared to another?
2. How do we find the amount of time it took for a group of segments to get compared to a song?


#Resource
1. [Python Time API]

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
 
 This essentially answers both questions that we have: "How long would it take to compare one segment to another? What about
 comparing one song to a group of segments?"

 [Python Time API]: https://docs.python.org/2/library/time.html
 
