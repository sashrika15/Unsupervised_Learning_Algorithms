import matplotlib.pyplot as plt

def plot(img):
  plt.title("Original Image")
  plt.imshow(img)
  plt.show()

def plot_svd(img_after_svd):
  plt.title("Image after applying SVD")
  plt.imshow((img_after_svd), cmap = 'gray')
  plt.show()  