### Density-Based Spatial Clustering of Applications with Noise (DBSCAN)

It is a clustering algorithm which focuses on the proximity and density of observations to form clusters.

### How does it work?

DBSCAN basically works by classifying each and every point in the dataset into one of three categories:
1. Core Point

A point is classified as core point if it has greater than or equal to a given minimum number of points within a given radius.

2. Edge Point

A point which is not classified as a core point i.e the number of neighbouring point within radius is less than the minimum number of points, but it had a core point present within the radius, that is known as an edge point.

3. Noise Point

All other points which are not edge or core points are known as noise points.

In the picture shown below, the red coloured points are the core points, the yellow coloured are the edge points and the blue coloured are the noise points.

<img src="https://github.com/sashrika15/Unsupervised_Learning_Algorithms/blob/master/DBSCAN/sample.gif" width="800">