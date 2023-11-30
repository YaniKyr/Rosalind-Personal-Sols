#Graph Generator with multi linked list
import sys
sys.setrecursionlimit(10000)
from collections import defaultdict
import math
upper = 99999999
class Node:


    def __init__(self,id):
        self.id = id
        self.neighbours = []
        self.edges =0
        self.cohesive_component = None

################### Dfs in order to find cohesive_components ######################

def Dfs(structure,coh):
    visited = [False for ver in structure]
    for ver in structure:
        if visited[ver.id-1] ==False:
            ver.cohesive_component =coh
            Explore(structure,ver.id,coh,visited)
            coh+=1

def Explore(structure,vertex,coh,visited):
    visited[vertex-1] = True
    for edge in structure[vertex-1].neighbours:
        if visited[edge.id-1] == False:

            edge.cohesive_component =coh

            Explore(structure,edge.id,coh,visited)

######################### Dijkstra################################################



def FindCost(mapp,u,v):
    for ele in mapp:

        if ele[0] == v and ele[1] == u:
            return ele[2]

def Dijkstra(structure,ver,cost):
    Q = []
    prev=[]
    dist =[]
    for ele in structure:
        dist.append(upper)
        prev.append(None)

    dist[ver-1] = 0

    Q.append(structure[ver-1])
    while Q:
        lista = [i.id for i in Q]
        minimum = lista.index(min(lista))

        u = Q.pop(minimum)

        for ele in  u.neighbours:


            if dist[ele.id-1] > dist[u.id-1] + FindCost(cost,ele.id,u.id):
                #print("Im here")
                #print( FindCost(cost,ele.id,u.id),"=>", dist[u.id-1],"==",dist[ele.id-1],"==",Q)
                dist[ele.id-1] = dist[u.id-1] + FindCost(cost,ele.id,u.id)
                prev[ele.id-1] = u
                Q.append(ele)

    for i in range(len(dist)):
        if dist[i] == upper:
            dist[i]=-1
    return dist

def Make_Graph(data,vertex):
    comp =1
    with open(data,'r') as f:
        file = f.read()
    mapp = [int(i) for i in file.split()]
    vertices = mapp[0]
    edges = mapp[1]
    cost=[]
    arr = [(mapp[i],mapp[i+1],mapp[i+2]) for i in range(2,len(mapp),3)]

    cost = [i[2] for i in arr]
    listoVertices = [Node(i+1) for i in range(vertices)]

    for i in range(0,edges):
        listoVertices[arr[i][0]-1].neighbours.append(listoVertices[arr[i][1]-1])


    dist = Dijkstra(listoVertices,1,arr)

    return listoVertices,dist

######################### BFS  ################################################

def Bfs(structure,vertex):
    dist  = defaultdict()
    for index in structure:
        dist[index.id-1] = upper

    queue = []

    dist[vertex-1]= 0
    queue.append(vertex)
    while queue:
        u = queue.pop(0)
        for ele in  structure[u-1].neighbours:
            if dist[ele.id-1] == upper:
                queue.append(ele.id)
                dist[ele.id-1] = dist[u-1] +1
    for i,vals in enumerate(dist.values()):
        if vals == upper:
            dist[i] = -1
    return dist
###########################################################################

#def Search(structure,val):
     #for i in range(0,len(structure)):

        #print(structure[i].cohesive_component,"=>",structure[i].id)


#============================Create Graph with bidirectional edges=======================
def FindNeighbors(data):
    comp =1
    with open(data,'r') as f:
        file = f.read()
    mapp = [int(i) for i in file.split()]
    vertices = mapp[0]
    edges = mapp[1]
    arr = mapp[2:]

    listoVertices = [Node(i+1) for i in range(vertices)]

    for i in range(0,edges):

        listoVertices[arr[2*i]-1].edges+=1
        listoVertices[arr[2*i+1]-1].edges+=1


        listoVertices[arr[2*i]-1].neighbours.append(listoVertices[arr[2*i+1]-1])
        listoVertices[arr[2*i+1]-1].neighbours.append(listoVertices[arr[2*i]-1])



    #for i in range(len(listoVertices)):
    #    print("ID:",listoVertices[i].id," ->",listoVertices[i].neighbours," Edges:",listoVertices[i].edges)

    sums = [0 for i in range(vertices)]
    for i in range(len(listoVertices)):
        for element in listoVertices[i].neighbours:
            ele = element.id
            sums[i] += listoVertices[ele-1].edges


    return listoVertices


def UndirectedGraph(data):
    comp =1
    with open(data,'r') as f:
        file = f.read()
    mapp = [int(i) for i in file.split()]
    vertices = mapp[0]
    edges = mapp[1]
    arr = mapp[2:]

    listoVertices = [Node(i+1) for i in range(vertices)]

    for i in range(0,edges):

        listoVertices[arr[2*i]-1].edges+=1



        listoVertices[arr[2*i]-1].neighbours.append(listoVertices[arr[2*i+1]-1])
        listoVertices[arr[2*i+1]-1].neighbours.append(listoVertices[arr[2*i]-1])



    #for i in range(len(listoVertices)):
    #    print("ID:",listoVertices[i].id," ->",listoVertices[i].neighbours," Edges:",listoVertices[i].edges)

    sums = [0 for i in range(vertices)]
    for i in range(len(listoVertices)):
        for element in listoVertices[i].neighbours:
            ele = element.id
            sums[i] += listoVertices[ele-1].edges


    return listoVertices

def DirectedGraph(data):
    comp =1
    with open(data,'r') as f:
        file = f.read()
    mapp = [int(i) for i in file.split()]
    vertices = mapp[0]
    edges = mapp[1]
    arr = mapp[2:]

    listoVertices = [Node(i+1) for i in range(vertices)]

    for i in range(0,edges):

        listoVertices[arr[2*i]-1].edges+=1



        listoVertices[arr[2*i]-1].neighbours.append(listoVertices[arr[2*i+1]-1])




    #for i in range(len(listoVertices)):
    #    print("ID:",listoVertices[i].id," ->",listoVertices[i].neighbours," Edges:",listoVertices[i].edges)

    sums = [0 for i in range(vertices)]
    for i in range(len(listoVertices)):
        for element in listoVertices[i].neighbours:
            ele = element.id
            sums[i] += listoVertices[ele-1].edges


    return listoVertices
