import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse


class GaussianMixtureModel:
    def __init__(self, num_clusters, num_iters, data):
        
        # Number of desired clusters
        self.num_clusters = num_clusters
        # Number of iteration to run the model for
        self.num_iters = num_iters

        # List containing Log-Likelihood per iteration
        self.log_likelihood = []

        # Initializing weights
        self.weights = [1 / self.num_clusters for cluster in range(self.num_clusters)]
        
        # Data Init
        self.data = data
        self.num_samples, self.num_features = self.data.shape
        self.data_len = len(self.data)

        split_data = np.array_split(self.data, self.num_clusters)

        self.mean_vector = [np.mean(x, axis=0) for x in split_data]
        self.covariance_mat = [np.cov(x.T) for x in split_data]

        # Computing gaussian for given mean and covariance
        self.multi_gaussian = lambda mu, cov : np.linalg.det(cov) ** (-0.5) * (2 * np.pi) ** (self.data.shape[1] * -0.5) \
                                               * np.exp(-0.5 * np.einsum('ij, ij -> i', self.data - mu, \
                                                 np.dot(np.linalg.inv(cov), (self.data - mu).T).T ) )
        
            
    
    def fit(self):
        ''' Fitting the Gaussian Mixture Model to the Data'''
        
        for iteration in range(self.num_iters):

            '''Estimation Step'''

            # Initializing Responsibility Matrix
            self.responsibility_matrix = np.zeros((self.data_len, self.num_clusters))

            # For each cluster, compute responsibility value
            for i in range(self.num_clusters):
                self.responsibility_matrix[:, i] = self.multi_gaussian(self.mean_vector[i], self.covariance_mat[i])
            
            # Computing the log likelihood which is being maximized by the formula, to keep track.

            log_likelihood = np.sum(np.log(np.sum(self.responsibility_matrix, axis = 1)))
            self.log_likelihood.append(log_likelihood)

            # The Responsibility Matrix is then normalized (This is a vectorized form)
            self.responsibility_matrix = (self.responsibility_matrix.T / np.sum(self.responsibility_matrix, axis = 1)).T
            
            # N is a list of the sum of each values in a column of the responsibility matrix
            N = np.sum(self.responsibility_matrix, axis=0)
            
            '''Maximization Step'''
            # In this step we maximizes the log-likelihood found at the Expectation step.
            for i in range(self.num_clusters):
                
                self.mean_vector[i] = 1.0 / N[i] * np.sum(self.responsibility_matrix[:, i] * self.data.T, axis = 1).T
                
                data_mean_normalized = np.matrix(self.data - self.mean_vector[i])

                # The longer dot product is basically the computation of the covariance.

                self.covariance_mat[i] = np.array(1 / N[i] * np.dot(np.multiply(data_mean_normalized.T,  self.responsibility_matrix[:, i]), data_mean_normalized))
                
                # The weights are updated
                self.weights[i] = 1.0 / self.data.shape[0] * N[i]
    

    def predict_cluster(self, x = None):
        
        self.multi_gaussian_prediction = lambda mu, cov:  np.linalg.det(cov) ** (-0.5) * (2 * np.pi) ** (len(x) * -0.5) \
                                                            * np.exp(-0.5 * np.dot(x - mu, np.dot(np.linalg.inv(cov), (x - mu).T).T ) )
        
        probs = np.array([w * self.multi_gaussian_prediction(mu, cov) for mu, cov, w in zip(self.mean_vector, self.covariance_mat, self.weights)])

        return np.argmax(probs / np.sum(probs), axis=0)
    

    def plot_clusters(self, plot_log_likelihood = True):            
        
        if self.num_features <= 2:
            def plot_ellipse(pos, cov, nstd=2, ax=None, **kwargs):
                def eigsorted(cov):
                    vals, vecs = np.linalg.eigh(cov)
                    order = vals.argsort()[::-1]
                    return vals[order], vecs[:,order]
            
                if ax is None:
                    ax = plt.gca()
            
                vals, vecs = eigsorted(cov)
                theta = np.degrees(np.arctan2(*vecs[:,0][::-1]))
            
                # Width and height are "full" widths, not radius
                width, height = 2 * nstd * np.sqrt(abs(vals))
                ellip = Ellipse(xy=pos, width=width, height=height, angle=theta, **kwargs)
            
                ax.add_artist(ellip)
                return ellip 

            def show(X, mu, cov):
                    plt.cla()
                    K = len(mu) # number of clusters
                    colors = ['b', 'k', 'g', 'c', 'm', 'y', 'r']
                    plt.plot(X.T[0], X.T[1], 'm*')
                    for k in range(K):
                        plot_ellipse(mu[k], cov[k],  alpha=0.6, color = colors[k % len(colors)])  


            fig = plt.figure(figsize = (13, 6))
            
            if plot_log_likelihood is True:
                fig.add_subplot(121)
                show(X = self.data, mu = self.mean_vector, cov = self.covariance_mat)
                fig.add_subplot(122)
                plt.plot(np.array(self.log_likelihood))
                plt.title('Log Likelihood vs iteration plot')
                plt.xlabel('Iterations')
                plt.ylabel('log likelihood')
                plt.show()
            else:
                show(X = self.data, mu = self.mean_vector, cov = self.covariance_mat)

        else:
            print("Cannot plot for higher dimensional data currently, my sincere apologies. :(")

