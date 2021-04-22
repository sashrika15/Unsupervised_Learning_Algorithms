from src.msc_scratch import Mean_Shift
from src.view import output

import matplotlib.pyplot as plt
from matplotlib import style
#import numpy as np
style.use('ggplot')
from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=15, centers=3, n_features=2)
#if you want to try it with personalised dataset,
#comment line 9 and 11 and uncomment line 17 till line 35
'''X = np.array([[2, 5],
                  [1.5, 6],
                  [1.5, 5.5],
                  [1, 4],
                  [3, 4.5],
                  [10, 7],
                  [9, 8],
                  [9.5, 7.5],
                  [9, 6.5],
                  [8, 7.5],
                  [3, 10],
                  [3.5, 9],
                  [2.5, 10],
                  [2, 10],
                  [2.3, 9.5],
                  [7, 1],
                  [6.5, 1],
                  [8, 2],
                  [6, 3],
                  [7.5, 3], ])'''

colors = 10 * ["g", "r", "c", "b", "k"]

#calling the Mean Shift Clustering function, check src/msc_scratch.py for it's working from scratch
Mean_Shift()

clf = Mean_Shift()
clf.fit(X)

centroids = clf.centroids
print(centroids)

#plotting the classified data points and their centroids
output(clf, colors, centroids)

plt.show()