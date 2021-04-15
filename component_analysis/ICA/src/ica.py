import numpy as np
from utils import *

def ica(X, iterations, limit = 1e-5):
  X = center(X)
  X = whiten(X)
  dim = X.shape[0]
  W = np.zeros((dim, dim), dtype=X.dtype)
  for i in range(dim):
    w = np.random.rand(dim)
    for j in range(iterations):
      w_new = update_w(w, X)
      if i >= 1:
	w_new -= np.dot(np.dot(w_new, W[:i].T), W[:i])
      distance = np.abs(np.abs((w * w_new).sum()) - 1)
      w = w_new
      if distance < limit:
	break
    W[i, :] = w
    S = np.dot(W, X)
  return S
