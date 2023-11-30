
class Node:
    def __init__(self,seq,id=None):
        self.seq = seq
        self.id  =id
        self.children = []
    
def strcmp(a,b):
    print(a,b)
    match=[]
    for i,j in zip(a,b):
        if i==j:
            match.append(i)
    return match

def _insert(root,motif,index):
    count =0
    if not root.children:
        root.children.append(Node(motif,index))
        return
    for child in root.children:
        match = strcmp(child.seq,motif)
        if match:
            pass
        else:
            count+=1

    if count == len(match):
        root.children.append(Node(motif,index))
            
                
def print_tree(root, level=0):
    if root is None:
        return
    print('    ' * level + f'+-- {root.seq}')
    for child in root.children:
        print_tree(child, level+1)
                   
                
                


def createSuffixT(string):
    array = []
    root = Node("",None)
    for i in range(len(string)-1,-1,-1):
        array.append(string[i:])
    for i,ele in enumerate(array):
        _insert(root,ele,i)
        
    
    print(root)
    print_tree(root)
createSuffixT("BANANA$")
