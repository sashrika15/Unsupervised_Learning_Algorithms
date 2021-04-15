import numpy as np
import random

def assign(n_clusters, data):
  ''' Defining the initial Cluster Centroids '''

  np.random.seed(400)
  centroids = {
      i+1 : [int(data[0][np.random.randint(0,799),0]), int(data[0][np.random.randint(0,799),1])]
      for i in range(n_clusters)
  }
  return centroids

def cluster_assignment(X, centroids, k):
  ''' Cluster Assignment Step '''

  ''' The algorithm goes through each of the examples and depending on whether they are closer to one of the centroid,
      it assigns each of the data points to one of the cluster centroids '''

  clusters = {}
  # Set the range for value of k(number of cluster centroids)
  for i in range(k):
    clusters[i] = []
  # Setting the plot points using dataframe (X) and the norm 
  for i in X:
    # Set up list of euclidian distance and iterate 
    euclidian_dist = []
    for j in range(k):
      euclidian_dist.append(np.linalg.norm(i - centroids[j]))
    # Append the cluster of data (index of minimum euclidian distance) to the dictionary
    clusters[euclidian_dist.index(min(euclidian_dist))].append(i)
  return clusters


def move_centroid(centroids, clusters, k):
  ''' Move Centroid Step '''

  ''' The cluster centroids are taken and moved to the average of their corresponding data points. 
      Specifically, we are going to compute the mean of the points’ location for each of the two clusters already formed 
      and move the centroids to their respective cluster means '''

  for i in range(k):
    # Finds the average of the cluster at the particular index
    centroids[i] = np.average(clusters[i], axis=0)
  return centroids