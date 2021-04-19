import numpy as np
import pandas as pd
from sklearn import preprocessing

def pca(X):
  X = preprocessing.StandardScaler().fit_transform(X)
  X_cov = (X.T @ X) / (X.shape[0] - 1) #here we are taking our mean as 0 
  P_values, P = np.linalg.eig(X_cov)
  idx = np.argsort(P_values, axis=0)[::-1]
  cumsum = np.cumsum(P_values[idx]) / np.sum(P_values[idx])
  c=0
  for i in range(1,64):
      if cumsum[i]>0.95:
          c+=1
  X_pca = X.dot(P[:,0:25])
  return X_pca