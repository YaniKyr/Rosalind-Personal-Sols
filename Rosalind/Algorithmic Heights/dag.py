class Edge:


    def __init__(self,id):
        self.edge = id
        self.start = None
        self.end = None
class Node:
    def __init__(self,id) :
        self.id = id
        self.neighbour = []


def Dfs(structure):
    
    visited = [0 for _ in structure]
    for ver in structure:
        if visited[ver.id-1] <=1:
            
            Explore(structure,ver.id,visited)
    return visited    

def Explore(structure,vertex,visited):
    visited[vertex-1] +=1
    for edge in structure[vertex-1].neighbour:
        if visited[edge.id-1] <= 1:

            Explore(structure,edge.id,visited)

def DirectedGraph(data):
    comp =1
   
    for value in data.values():
        
        ver  = max(value, key=lambda sublist: sublist)[1]
       
        bagOfVertices =[Node(i+1) for i in range(ver)]
        for i,ele in enumerate(value):
            
            
            bagOfVertices[ele[0]-1].neighbour.append(bagOfVertices[ele[1]-1])
            
        temp = Dfs(bagOfVertices)
        numb = min(temp)
        print(temp)
        if numb<2:
            print(1,end=" ")
        else:
            print(-1,end=" ")

   


    #for i in range(len(listoVertices)):
    #    print("ID:",listoVertices[i].id," ->",listoVertices[i].neighbours," Edges:",listoVertices[i].edges)

    # sums = [0 for i in range(vertices)]
    # for i in range(len(listoVertices)):
    #     for element in listoVertices[i].neighbours:
    #         ele = element.id
    #         sums[i] += listoVertices[ele-1].edges


  

with open("testfile.txt",'r') as f:
    line  = f.read()
    dat = line.split('\n')
    
dicto = {k: [] for k in range(int(dat[0]))}
count =0
for ele in dat[2:]:
    if ele =='':
        count+=1   
    else:

        dicto[count].append([int(i) for i in ele.split()]) 

vertices = DirectedGraph(dicto)
