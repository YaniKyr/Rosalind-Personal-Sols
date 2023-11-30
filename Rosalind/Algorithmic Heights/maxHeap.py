

def heapify(heap, i):
   
    if i==0:
        return
    parent = (i-1)//2
    child = i
    if heap[parent] > heap[child]:
        return
    else:
        heap[parent], heap[child] = heap[child], heap[parent]
        heapify(heap, parent)
    
                
       
            
           


with open("testfile.txt", "r") as f:
    fil = f.read()
    file = fil.split("\n")
    n = int(file[0])
    data = [int(ele) for ele in file[1].split()]

def Main(data):
    heap = []
    sortedarr = []
    for i in range(len(data)):
        heap.append(data[i])
        heapify(heap,i)
    return heap
root = []
for i in range(n):

    temp = Main(data)
    root.append( temp.pop(0))
    data = temp
    