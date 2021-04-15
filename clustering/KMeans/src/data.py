from sklearn.datasets import make_blobs

def datagen(n_samples, centers, n_features):
  ''' Function to generate a toy dataset '''
  
  data = make_blobs(n_samples = n_samples, centers = centers, n_features = n_features, cluster_std = 1.5, shuffle = True, random_state = 50)
  return data