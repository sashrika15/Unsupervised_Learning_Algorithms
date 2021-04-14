import numpy as np
from scipy import signal
from matplotlib import pyplot as plt

def center(x):
  X = np.array(x)
  return X - X.mean(axis = 1, keepdims = True)
  
def whiten(X):
  x_cov = np.cov(X)  # covariance matrix
  d, E = np.linalg.eigh(x_cov)  # 'd' stores the eigen values which will be diagonalised, 'E' is the orthogonal matrix of eigenvectors
  D = np.diag(d)  # diagonal matrix of eigen values
  D_inv = np.sqrt(np.linalg.inv(D))
  return np.dot(E, np.dot(D_inv, np.dot(E.T, X)))
  
def g(x):
  return np.tanh(x)

def g_bar(x):
  return 1-(np.tanh(x))**2

def update_w(w, X):
  w_new = (X * g(np.dot(w.T, X))).mean(axis = 1) - g_bar(np.dot(w.T, X)).mean() * w
  return w_new/np.sqrt((w_new ** 2).sum())
