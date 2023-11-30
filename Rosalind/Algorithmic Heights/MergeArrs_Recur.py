def RecurCon(A,B,C):
    #Load the remaining elements
    if len(A)<1 or len(B)<1: 
        for i in A:
            C.append(i)
        for j in B:
            C.append(j)
        return

    if A[0] > B[0]:
        C.append(B[0])
        RecurCon(A,B[1:],C)
    else:
        C.append(A[0])
        RecurCon(A[1:],B,C)
   
    
    
    

import sys

with open("rosalind_mer (3).txt",'r') as f:
    file = f.read()
mat = [int(i) for i in file.split()]
n = mat[0]
A = mat[1:n+1]
m = mat[n+1]
B = mat[n+2:n+m+2]

sys.setrecursionlimit(m*n) # Set a new upper bound for the reccursion
C = []
RecurCon(A,B,C)

for out in C:
    print(out, '',end='')