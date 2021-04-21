# Self Organizing Maps (SOMs)
Self-Organizing Maps or SOMs is an Unsupervised Machine Learning Algorithm which reduces the dimensionality of the input so as to represent it in a map.

It is very similar to the general Artificial Neural Network, but with one small tweak. Unlike an ANN, which learns by backpropogation, SOMs, implement the concept of Competitive Learning to learn the weights. In Competitive Learning the Output Neurons of the hidden layer compete amongst themselves to be activated, and there can only be one neuron that can be activated at any given time.

This algortithm was invented by Teuvo Kohonenin the 1980s and is sometimes called Kohonen Maps.

With the help of Python, I have implemented the working of a simple Self-Organizing Map where I'll be using a dataset of random colours which are represented as 3D vectors (Each colour of the vector representing R,G,B values) and visualise the different clusters we can form with it in a 2D space.

It will look similar to this:

![2000 Iterations 2](https://user-images.githubusercontent.com/70643852/96720572-8f177c00-13c8-11eb-8079-ead90cb4c780.png)

You can refer to this [Notebook](https://github.com/Pranav1007/SOMs/blob/main/notebook/Intution%20behind%20SOMs.ipynb) for the implementation

# Applications of Self Organizing Maps
* Clustering Problems
* Dimensionality Reduction
* Visualising Higher Dimensions in 2D space

# Examples of Colour Quantization using SOMs:
With the help of the [MiniSom Library](https://github.com/JustGlowing/minisom) I have implemented a colour quantization model. Basically, this model will use Self Organizing Maps to reduce the number of distinct colours present in the image in such a way that the new image is still visually similar to the original image.

![Image1](https://user-images.githubusercontent.com/70643852/115564921-8c91d280-a2d6-11eb-9e5d-91fc716f90f9.png)

![Image2](https://user-images.githubusercontent.com/70643852/115565016-a3382980-a2d6-11eb-8c43-2bf3ded1a895.png)

![Image3](https://user-images.githubusercontent.com/70643852/115565080-b21edc00-a2d6-11eb-945f-daf4bbe4de7e.png)

# How to Use the Repo and obtain these Images in your Local Device

- Clone the GitHub repository
```python
$ git clone git@github.com:Pranav1007/SOMs.git
```

- Move to the SOMs Directory
```python
$ cd SOMs
```

- All the [requirements](requirements.txt) and dependencies need to be installed. 
```python
$ pip install -r requirements.txt
```

- Run the test file now to see the Colour Quantized Image
```python
$ python test.py
```

Contributed by: 

[Pranav B Kashyap](https://github.com/Pranav1007)
