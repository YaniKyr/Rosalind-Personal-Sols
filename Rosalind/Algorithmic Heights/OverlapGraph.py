with open("rosalind_grph (6).txt",'r') as f:
    file = f.read()
arr = file.split()


vertices = {}
nodes = []
for i in range(0,len(arr),3):
    vertices[arr[i]] = arr[i+1]+arr[i+2]
    nodes.append(arr[i])

for node in nodes:  
    suffix = vertices[node][-3:]

    for ele in nodes:
        
        preffix = vertices[ele][0:3]
        
        if node == ele:
            continue
        if preffix ==suffix:
            print(node[1:],"",ele[1:])
    
    

    