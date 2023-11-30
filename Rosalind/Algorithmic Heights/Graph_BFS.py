from collections import defaultdict

data='''6 6
4 6
6 5
4 3
3 5
2 1
1 4'''

matrix = data.split()
n_vertices = matrix[0]
n_edges = matrix[1]
graph = defaultdict(list)
edges = [int(ele) for ele in matrix[2:]]
for i in range(0,len(edges)-1,2):
    graph = defaultdict([edges[i],edges[i+1]])