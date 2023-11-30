
import DDArray as dd

file = "sample.txt"


class BFS:
    def __init__(self,graph):
        self.graph =graph
    
    def Solve(self,start):
        queue = []
        visited = []
        visited.append(self.graph[start-1])
        queue.append(self.graph[start-1])

        while queue:
            m = queue.pop(0)
            print(m,end="")
            mid = m.id
            print('The id is :',mid)
            for neighbour in graph[mid-1]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
    def BuildPath(self,mat,start,end):
            pass
        #path reverse it 
        


graph = dd.FindNeighbors(file)
print(graph[2])
bfs = BFS(graph)

prev= bfs.Solve(1)
print(prev)
bfs.BuildPath(prev,0,5)

for sol in prev:
    if sol is None: continue
    print(sol.id)
