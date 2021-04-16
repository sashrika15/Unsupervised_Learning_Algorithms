import numpy as np
import matplotlib.pyplot as plt
import queue



unassigned = 0
core = -1
border = -2

class DBSCAN:

    def __init__(self, data, radius, min_points):
        self.data = data
        self.radius = radius
        self.min_points = min_points

        #Initilize all points to unassigned
        self.point_label  = [unassigned] * len(self.data)

        #Stores neighbour points for each point
        #Essentially becomes  a list of list i.e if point 1 has 5 neighbours, it will be [[1,2,3,4,5], ...] and so on
        self.neighbour_points = []   
    
    
    def find_neighbor_points(self, point_id):
        '''
        Find neighbour points for each point in data
        Inputs:
        point_id : The point to be checked to see if it is neighbour or not
        Returns:
        points : List of neighbours for each point
        '''
        points = []
        for i in range(len(self.data)):
            #If distance between two points is less than given radius, then it is neighbour point
            if np.linalg.norm(self.data[i] - self.data[point_id]) <= self.radius:
                points.append(i)
        return points

    def fit(self):
        '''
        Fit DBSCAN algorithm to data

        Returns:
        point_label: List of label for each point in dataset. (Labels start from 1,2,.. and go on to number of clusters)
        cluster: Number of clusters

        '''
        core_points, noncore_points = self.label_points()
        cluster = 1

        #Using a Queue to put all neigbour core point in queue and find neigbour's neigbour
        for i in range(len(self.point_label)):
            q = queue.Queue()
            if (self.point_label[i] == core):
                self.point_label[i] = cluster  #If the point is core, you assign it to cluster
                for x in self.neighbour_points[i]:
                    if(self.point_label[x]==core):
                        q.put(x)       #Put neighbour core points in queue, since their neighbouring core points might also be part of cluster
                        self.point_label[x]=cluster    #Assign neighbour core point to cluster
                    elif(self.point_label[x]==border):    
                        #Border points also form part of cluster but they arent put in queue since their neighbours will not form cluster, they are border points
                        self.point_label[x]=cluster

                #Stop when all point in queue has been checked   
                while not q.empty():
                    neighbors = self.neighbour_points[q.get()]     #Get neighbour point
                    for y in neighbors:
                        if (self.point_label[y]==core):   
                            self.point_label[y]=cluster    #Check if it is core, assign to cluster then put in queue
                            q.put(y)
                        if (self.point_label[y]==border):
                            self.point_label[y]=cluster    #Border point also part of cluster    
                cluster+=1 #move to next cluster
            
        return self.point_label, cluster

    
    def label_points(self):
        '''
        Labels points as core or border and returns list of core points and noncore points
        Returns:
        core_points : List of core points
        noncore_points : List of noncore points 
        '''

        #Initilize list for core/noncore point
        core_points=[]
        noncore_points=[]
        
        #Find all neigbour for all points
        for i in range(len(self.data)):
            self.neighbour_points.append(self.find_neighbor_points(i))

        #Find all core points, edgepoints and noise points
        for i in range(len(self.neighbour_points)):
            if (len(self.neighbour_points[i])>=self.min_points):
                self.point_label[i]=core      #If there are more than minpoints in the neighbourhood of given point, it is core point
                core_points.append(i)
            else:
                noncore_points.append(i)       #Else it is non core point

        for i in noncore_points:
            for j in self.neighbour_points[i]:
                if j in core_points:
                    self.point_label[i]=border      #For noncore points, if the neighbourhood has one core point, then it is border point
                    break
        return core_points, noncore_points


    def plot_result(self, data, pointlabels, num_clusters):
        '''
        Function to plot result using different colours for each cluster
        Inputs: 
        Data : Dataset
        pointlabels : List of labels of each point
        num_clusters : Number of clusters

        '''
        cluster_colours = ['black', 'green', 'brown', 'red', 'purple', 'orange', 'yellow']
        for i in range(num_clusters):
            # Assigning colours to each cluster
            if i==0:
                #Plot all noise point as blue
                colour='blue'
            else:
                colour = cluster_colours[i % len(cluster_colours)]
            
            x = []  
            y = []
            for j in range(len(data)):
                if pointlabels[j] == i:
                    x.append(data[j, 0])
                    y.append(data[j, 1])
            plt.scatter(x, y, c=colour, alpha=1, marker='.')
        plt.title("DBSCAN")
        plt.show()
