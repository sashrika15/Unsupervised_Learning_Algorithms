from src.svd import *
from src.plot import *

import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

path = 'media/dog.jpg'
img = Image.open(path)
img_grayscale = img.convert('LA')
plot(img_grayscale)
imgmat = np.array( list(img_grayscale.getdata(band = 0)), float)
imgmat.shape = (img_grayscale.size[1], img_grayscale.size[0])
imgmat = np.matrix(imgmat)
comp_image = svd(imgmat,50)
plot_svd(comp_image)
