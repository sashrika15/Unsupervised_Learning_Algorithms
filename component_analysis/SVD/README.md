# Singular Value Decomposititon

The singular value decomposition of a matrix A is the factorization of A into the product of three matrices *A = UDV^(T)* where the columns of U and V are orthonormal and the matrix D is diagonal with positive real entries. The diagonal entries Sigma or S are known as the singular values of M. The number of non-zero singular values is equal to the rank of M. The columns of U and the columns of V are called the left-singular vectors and right-singular vectors of M, respectively.

It can also be thought of as a study of a matrix by studying it's most fundamental components like it's eigen vectors with an added advantage that the matrix need not be a sqaure matrix unlike PCA.

## Matrices U, V and S ##

- The matrix U is the eigen vector matrix of A^(T)A.

- The matrix V is the eigen vector matrix of AA^(T).

- The matrix S is a rectangular diagonal matrix with it's diagonal elements as the square root of the eigen values of U or V (both of them have the same eigen values) also          termed as the singular values of matrix A.
     
## How it works!! ##

SVD has it's use varying across a wide variety of domains. Here, we are using it for Image Compression for our demonstration purpose. Image compression with SVD is a frequently occurring application of this method. The image is treated as a matrix of pixels with corresponding color values and is decomposed into smaller ranks that retain only the essential information that comprises the image. 

The method of image compression with singular value decomposition is based on the idea that if the SVD is known, some of the singular values σ are significant while the others are small and not significant. Thus, if the significant values are kept and the small values are discarded then only the columns of U and V corresponding to the singular values are used.

As we increase the rank, the quality of the image increases.

This project is a mathematical analysis of SVD applied on an image given by the user.

## Applications
- Matrix Approximation

- Image Processing
    - Image Compression

## Original Image
<p align="left">
     <img src = "/component_analysis/SVD/media/dog_grayscale.png">
 
## Image after applying SVD
<p align="left">
    <img src = "/component_analysis/SVD/media/image_after_svd.png">

## To use this repo please follow the steps mentioned below

- Setting up the Python Environment with dependencies:

        pip install -r requirements.txt

- Cloning the Repository: 

        git clone https://github.com/sashrika15/Unsupervised_Learning_Algorithms
- Entering the Singular Value Decomposititon directory: 

        cd component_analysis/SVD
- Running the file:

        python3 test.py
        
Contributed by: <a href="https://github.com/indiradutta">Indira Dutta</a>
