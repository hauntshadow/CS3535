#Problem
We want to graph and learn the exact number of items in a bar (via bar plot).
This graph represents the number of items equal or greater than the lower limit, but smaller than the next lower limit.

#Questions
1. How do we get the data rounded to the lower limit?
2. How do we graph the data?
3. How do we list the number of items in each range?

#Resources
1. [Python math Module API]
2. [Using Counter() in Python to build histogram]
3. [Counter Objects]

####Mini-abstract and relevance of the [Python math Module API]
 The [Python math Module API] is the documentation I found when finding out how to get the floor of a number.
 Math.floor(num) returns the floor of that number.  That will be useful when computing the data's lower limit.
 
 The following code shows how to round a number (x) to the nearest value below it that is a multiple of y:
 ```python
 import math
 
 floored = math.floor(x)
 int(floored - (int(floored) % y))
 ```
This bit of code essentially answers Question 1 for us: "How do we get the data rounded to the lower limit?"
 
 
####Mini-abstract and relevance of [Using Counter() in Python to build histogram]

Python's Collections Module has a tool known as [Counter].  These objects simply count over an iterable collection, and return the number of occurrences of every item in the collection.  This can be useful in producing the bars in the graph.

The following code, according to the source, will plot a bar plot using the values from the [Counter] object:
 
 ```python
 from collections import Counter
 import numpy as np
 import matplotlib.pyplot as plt
 #Assume the array has been produced from the previous bit of code.
 a = [5, 5, 5, 10, 10, 15, 25, 25, 25, 25, 40]
 numbers, counts = zip(*Counter(a).items())
 indices = np.arange(len(labels))
 plt.bar(indices, counts, 1)
 plt.xticks(indexes + 0.5, labels)
 plt.show()
 ```
The code takes an array, then uses the zip() function to get the items as tuples of numbers and the number of occurrences that the [Counter] object returns.  Afterwards, the indices are received, then plotted with the counts.  The xticks function puts the labels on the x-axis, and the final graph is shown.

This answers our 2nd Question: "How do we graph the data?"
 
####Mini-abstract and relevance of [Counter Objects]
 
This documentation talks about how to get the actual numbers from the [Counter] object.  While there are many things that [Counter] can do with data representation, we want to be able to grab counts coupled with their elements.  This can be done by doing the following code:

```python
from collections import Counter
obj = Counter([5, 5, 5, 10, 10, 15, 15, 15, 25, 25, 40]
objAsList = obj.items()
print objAsList
```
This code converts the [Counter] object's data into a list using obj.items().  Then, you can simply print the list, which gets us our actual values.

Thus, Question 3 has been answered: "How do we list the number of items in each range?"


[Python math Module API]: https://docs.python.org/2/library/math.html
[Counter]: https://docs.python.org/3/library/collections.html#counter-objects
[Using Counter() in Python to build histogram]: http://stackoverflow.com/questions/19198920/using-counter-in-python-to-build-histogram
[Counter Objects]: https://docs.python.org/3/library/collections.html#counter-objects
