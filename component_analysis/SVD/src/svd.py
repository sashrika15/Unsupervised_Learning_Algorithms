import numpy as np

def svd(A, i):
  Ui = A.dot(A.transpose())
  Vi = A.transpose().dot(A)
  eig_values, U = np.linalg.eig(Ui)
  U = U.real
  eig_values.real
  V_eig_values, V = np.linalg.eig(Vi)
  V = V.real
  V_eig_values.real
  Si = np.diag(eig_values)  #Diagonal matrix with the diagonal elements as the eigen values
  Si = np.sqrt(Si)
  S = np.zeros((A.shape[0], A.shape[1]))  #Creating a rectangular matrix that'll act as the base for the actual Sigma matrix
  S[:A.shape[0], :A.shape[0]] = Si 
  comp_image = np.dot(U[:,:i],(np.dot(S[:i,:i],V[:,:i].transpose())))
  return comp_image