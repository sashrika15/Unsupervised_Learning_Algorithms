from gmm import GaussianMixtureModel
from sklearn.datasets import make_blobs
import numpy as np

X, y = make_blobs(n_samples = 100, n_features= 3)

gmm = GaussianMixtureModel(num_clusters = 5, num_iters = 1000, data = X)

gmm.fit()

print(gmm.predict_cluster(x = np.array([1, 2, 3])))

gmm.plot_clusters()
