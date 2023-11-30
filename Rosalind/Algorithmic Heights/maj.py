#Majority Element
#sort 
#find 
def Majority(array,k,n):
    majority = []
    total = 0
    for i  in range(k):
        count=0
        temp =0
        status = False
        arr = sorted(array[i])
        temp = arr[0]
        for ele in arr:
            total+=1
            
            if temp == ele:
                count+=1
            else:
                
                temp = ele
                count = 0
            if count > n//2:
                status = True
                
                count = 0
                break
        if status:
            print(temp,end=" ")
        else:
            print(-1,end=" ")
            
            

                


with open("testfile.txt", "r") as f:
    k, n = map(int, f.readline().strip().split())
    A = [[int(i) for i in line.strip().split()] for line in f]

Majority(A,k,n)