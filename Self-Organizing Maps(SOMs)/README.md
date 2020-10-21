**Self-Organizing Maps (SOMs)**

Self-Organizing Maps or SOMs is an Unsupervised Machine Learning Algorithm which reduces the dimensionality of the input so as to represent it in a map.

It is very similar to the general Artificial Neural Network, but with one small tweak. 
Unlike an ANN, which learns by backpropogation, SOMs, implement the concept of Competitive Learning to learn the weights. In Competitive Learning the Output Neurons of the hidden layer compete amongst themselves to be activated, and there can only be one neuron that can be activated at any given time.

This algortithm was invented by Teuvo Kohonenin the 1980s and is sometimes called Kohonen Maps.

With the help of Python, I have implemented the working of a simple Self-Organizing Map where I'll be using a dataset of random colours which are represented as 3D vectors (Each colour of the vector representing R,G,B values) and visualise the different clusters we can form with it in a 2D space.

It will look similar to this:


![2000 Iterations 2](https://user-images.githubusercontent.com/70643852/96720572-8f177c00-13c8-11eb-8079-ead90cb4c780.png)

