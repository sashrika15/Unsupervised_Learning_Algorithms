import PIL
from PIL import Image,ImageDraw
import math

def readfile(file):
  with open(file) as f:
    lines = f.readlines()

  col=lines[0].strip().split('\t')[1:]
  row=[]
  data=[]
  for line in lines[1:]:
    p=line.strip().split('\t')
    row.append(p[0])
    data.append([float(x) for x in p[1:]])
  return row,col,data

def pscore(v1,v2):
  
  sum1=sum(v1)                                                                         #sum
  sum2=sum(v2)
  sumSq1=sum([pow(v,2) for v in v1])                                                   #sum of squares
  sumSq2=sum([pow(v,2) for v in v2])	
  sumPr=sum([v1[i]*v2[i] for i in range(len(v1))])                                     #sum of products
  num=sumPr-(sum1*sum2/len(v1))
  den=math.sqrt((sumSq1-pow(sum1,2)/len(v1))*(sumSq2-pow(sum2,2)/len(v1)))             #pearson score
  if den==0: 
    return 0
  r=num/den
  return 1.0-r

class bicluster:                                                                      #rows and columns with almost same score
  def __init__(self,vec,left=None,right=None,distance=0.0,id=None):
    self.left=left
    self.right=right
    self.vec=vec
    self.id=id
    self.distance=distance

def hierarchical_cluster(rows,distance=pscore):
  distances={}
  curid=-1
  cluster=[bicluster(rows[i],id=i) for i in range(len(rows))]
  
  while len(cluster)>1:
    lowestpair=(0,1)
    closest=distance(cluster[0].vec,cluster[1].vec)
    
    for i in range(len(cluster)):                                                       #to find smallest distance among all the pairs
      for j in range(i+1,len(cluster)):
        if (cluster[i].id,cluster[j].id) not in distances: 
          distances[(cluster[i].id,cluster[j].id)]=distance(cluster[i].vec,cluster[j].vec)

        d=distances[(cluster[i].id,cluster[j].id)]

        if d<closest:
          closest=d
          lowestpair=(i,j)
    avg=[(cluster[lowestpair[0]].vec[i]+cluster[lowestpair[1]].vec[i])/2.0 for i in range(len(cluster[0].vec))]             #average of two clusters
    new=bicluster(avg, left=cluster[lowestpair[0]], right=cluster[lowestpair[1]], distance=closest, id=curid)               #new cluster

    # cluster ids that weren't in the original set are negative                       
    curid-=1
    del cluster[lowestpair[1]]
    del cluster[lowestpair[0]]
    cluster.append(new)

  return cluster[0]

def printcluster(cluster,labels=None,n=0):
  for i in range(n):                                                                   
    print (' '),
  if cluster.id<0:                                                                    #branch
    print ('-')
  else:                                                                               #endpoint
    if labels==None: 
      print (cluster.id)
    else: 
      print ("this",labels[cluster.id])

  #branches
  if cluster.left!=None: 
    printcluster(cluster.left,labels=labels,n=n+1)
  if cluster.right!=None: 
    printcluster(cluster.right,labels=labels,n=n+1)

def getheight(cluster):
  if cluster.left==None and cluster.right==None:                                     #endpoint
    return 1
  return getheight(cluster.left)+getheight(cluster.right)                            #get height of branch

def getdepth(cluster):
  if cluster.left==None and cluster.right==None:                                     #endpoint
    return 0
  return max(getdepth(cluster.left),getdepth(cluster.right))+cluster.distance        #sum of maximum of the two branches and the distance

#dendrogram
def dendrogram(cluster,labels,jpeg='clusters.jpg'):

  h=getheight(cluster)*20
  w=1200
  depth=getdepth(cluster)
  scaling=float(w-150)/depth
  img=Image.new('RGB',(w,h),(255,255,255))
  draw=ImageDraw.Draw(img)

  draw.line((0,h/2,10,h/2),fill=(255,0,0))    

  drawnode(draw,cluster,10,(h/2),scaling,labels)                                      #first node
  img.save(jpeg,'JPEG')

def drawnode(draw,cluster,x,y,scaling,labels):

  if cluster.id<0:
    h1=getheight(cluster.left)*20
    h2=getheight(cluster.right)*20
    top=y-(h1+h2)/2
    bottom=y+(h1+h2)/2
    ll=cluster.distance*scaling

    #vertical line   
    draw.line((x,top+h1/2,x,bottom-h2/2),fill=(255,0,0)) 

    #horizontal lines
    draw.line((x,top+h1/2,x+ll,top+h1/2),fill=(255,0,0))                             #left item
    draw.line((x,bottom-h2/2,x+ll,bottom-h2/2),fill=(255,0,0))                       #right item

    #draw the nodes
    drawnode(draw,cluster.left,x+ll,top+h1/2,scaling,labels)                         #left node
    drawnode(draw,cluster.right,x+ll,bottom-h2/2,scaling,labels)                     #right node
  else:   
    draw.text((x+5,y-7),labels[cluster.id],(0,0,0))                                   #endpoint

def rotatematrix(data):
  newdata=[]
  for i in range(len(data[0])):
    newrow=[data[j][i] for j in range(len(data))]
    newdata.append(newrow)
  return newdata
