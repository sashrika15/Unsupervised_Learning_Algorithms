import matplotlib.pyplot as plt

def view_clusters(centroids, clusters, k):
  colors = ['blue' ,'orange', 'cyan', 'red', 'green', 'yellow', 'gray']
  plt.figure(figsize = (6, 4)) 
  for i in range(k):
    for cluster in clusters[i]:
        plt.scatter(cluster[0], cluster[1], c=colors[i % k], alpha=0.6)          
    plt.scatter(centroids[i][0], centroids[i][1], c='gray', s=200)