from dbscan import DBSCAN
from sklearn.datasets import make_moons


x, _ = make_moons(n_samples=300, noise=0.1)



radius = 0.2
min_points = 10

print('Radius = '+str(radius)+', Minpoints = '+str(min_points))

model = DBSCAN(x, radius, min_points)

#Fitting model to dataset
point_labels, clusters = model.fit()

print('Number of clusters: ' + str(clusters-1))

#Plotting result
model.plot_result(x, point_labels, clusters)  