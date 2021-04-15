from src.kmeans import cluster_assignment, move_centroid
from src.data import datagen
from src.view import view_clusters

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

''' setting values of n_samples, centers, n_features '''

n_samples = 800
centers = 3
n_features = 2

''' generating the toy dataset '''
data = datagen(n_samples, centers, n_features)

''' defining the x and y coordinates in pandas dataframe '''
df = pd.DataFrame({
    'x': data[0][:,0],
    'y': data[0][:,1]
})

X = np.array(df[['x', 'y']])

''' setting value for n_clusters and iters '''
n_clusters = 3
centroids = {}
iter = 5

for i in range(n_clusters):
  centroids[i] = X[i*200]

for i in range(iter): 
  ''' cluster assignment step '''       
  clusters = cluster_assignment(X, centroids, n_clusters)

  '''move centroid step '''

  centroids = move_centroid(centroids, clusters, n_clusters)

  view_clusters(centroids, clusters, n_clusters)
