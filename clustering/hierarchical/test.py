import PIL
from PIL import Image,ImageDraw
from cluster import readfile, dendrogram, rotatematrix, hierarchical_cluster, printcluster

blognames,words,data = readfile('database.txt')
cluster = hierarchical_cluster(data)
printcluster(cluster,labels = blognames)

dendrogram(cluster,labels=blognames,jpeg='blogoutput.jpg')
rdata=rotatematrix(data)
wordcluster=hierarchical_cluster(rdata)
dendrogram(wordcluster,labels=words,jpeg='wordoutput.jpg')