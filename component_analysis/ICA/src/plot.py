import matplotlib.pyplot as plt

def plot_ica(X, original_sources, S):
  fig = plt.figure()
  plt.subplot(3, 1, 1)
  for x in X:
    plt.plot(x)
  plt.title("Mixed signals")
  plt.subplot(3, 1, 2)
  for s in original_sources:
    plt.plot(s)
  plt.title("Real source signals")
  plt.subplot(3,1,3)
  for s in S:
    plt.plot(s)
  plt.title("Predicted source signals")

  fig.tight_layout()
  plt.show()
