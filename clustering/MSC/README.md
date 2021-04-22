<h1>What is Mean Shift Clustering</h1>
MSC is a centroid based clustering algorithm which iteratively updates centroid in the data till blobs are discovered in the sample provided. It is a type of unsupervised machine learning algorithm. The algorithm works on the concept of Kernel Density Estimation known as KDE. It is also known as mode seeking algorithm.
This algorithm is mostly used for computer vision and image segmentation.

Mean-Shift algorithm basically assigns the datapoints to the clusters iteratively by shifting points towards the highest density of datapoints i.e. cluster centroid.

Basically it is a straightforward approach which primarily used to solve problems related to image segmentation, clustering. It is comparatively slower than K-Means and it is computationally expensive.

<h2>Working</h2>
<img src="images/steps.png" align="middle">

It is evident from the image that there are 3 clusters here.<br>
<img src="images/before.png" align="middle">


Results:
The algorithm runs perfectly and segments the 3 clusters with their respective centeroids.
<img src="images/after.png" >
