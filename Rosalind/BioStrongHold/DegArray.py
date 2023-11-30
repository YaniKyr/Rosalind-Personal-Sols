with open("rosalind_deg (1).txt",'r') as f:
    file = f.read()
edges = [int(i) for i in file.split()]
edges = edges[2:]
zero = [0 for i in range(max(edges))]
for edge in edges:
    zero[edge-1]+=1

for ele in zero:
    print(ele," ",end = "")