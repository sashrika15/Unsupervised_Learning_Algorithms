import numpy as np
import matplotlib.pyplot as plt

def read_img(image):
    img = plt.imread(image)
    data = np.reshape(img, (img.shape[0] * img.shape[1], img.shape[2]))
    return img, data
