'''
The problem is to find a given set of keys in a given array.

Given: Two positive integers n≤10^5 and m≤10^5, a sorted array A[1..n] of integers from −10^5 to 10^5 and a list of m 
integers −10^5≤k1,k2,…,km≤10^5.

Return: For each ki, output an index 1≤j≤n s.t. A[j]=ki or "-1" if there is no such index.'''

def BinSearch(bottom,top,arr,key,output):
    if(bottom>top):
        output.append('-1')
        return ;
    
    middle = int((top+bottom)/2)
    if int(arr[middle]) == int(key):
        output.append(f'{middle+1}')
    if int(arr[middle]) > int(key):
        BinSearch(bottom,middle-1,arr,key,output)
    elif int(arr[middle]) <int(key):
        BinSearch(middle+1, top, arr,key,output)

# with open("C:\\Users\\kiria\\OneDrive\\Υπολογιστής\\John\\rosalind_bins (9).txt",'r') as f:
#     file = f.read()
# mat = file.split()
# n = int(mat[0])
# m = int(mat[1])

# arr = mat[2:n+2]
# keys = mat[n+2:m]
# output = []
# for key in keys:
#     BinSearch(0,n-1,arr,key,output)    

# for out in output:
#     print(out, '',end='')