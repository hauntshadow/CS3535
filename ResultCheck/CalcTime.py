import numpy as np
from collections import Counter

def calculate(filename):
    data = np.load(filename)
    checked = data[1]
    countClusters = Counter()
    counter = Counter()
    for i in checked:
        countClusters[i] += 1
    for i in countClusters.values():
        counter[i] += 1
    val = counter.values()
    key = counter.keys()
    sum = 0
    for i in range(len(key)):
        sum += val[i] * key[i] ** 2
    sum += (len(checked) * len(countClusters.values()))
    print sum
    fin = sum * (4376.4/4999950000)
    print fin
