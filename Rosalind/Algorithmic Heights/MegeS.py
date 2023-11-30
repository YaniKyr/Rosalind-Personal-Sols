def Merge(arr,l, m,r):
    n1 = m-l+1
    n2 = r-m
    L = [] 
    R = [] 
    for i in range(n1):
        L.append( arr[l+i])
    for j in range(n2):
        R.append(arr[m+1+j])

    i=j=0
    k=l
    while i<n1 and j <n2:
        if L[i] <= R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1
    
    while i<n1:
        arr[k]=L[i]
        i+=1
        k+=1
    while j<n2:
        arr[k] = R[j]
        j+=1
        k+=1

def mergeSort(arr,l,r):
    if l<r:
        m = l+(r-l)//2
        
        mergeSort(arr,l,m)
        mergeSort(arr,m+1,r)
        Merge(arr,l,m,r)
    
# with open("rosalind_ms.txt",'r') as f:
#     file = f.read()
# mat = file.split()
# n= int(mat[0])
# arr = [int(i) for i in mat[1:]]
# mergeSort(arr,0,n-1)

# for ele in arr:
#     print(ele," ", end ="")