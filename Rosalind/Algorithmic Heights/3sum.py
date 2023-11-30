
def three_sum(a, target=0):
   
    tmp_dict = {}
    for i,ele in enumerate(a):
        if ele in tmp_dict:
            
            tmp_dict[ele].append(i)
        else:
            tmp_dict[ele]=[i]
    flag=0
    for ele in tmp_dict:
        
        q,r=[],[]
        if ele <0:
            flag=1
            for i in range(-ele):
                if i in tmp_dict:
                    substitute = -(ele +i)
                    if substitute in tmp_dict:
                        
                      
                        if tmp_dict[ele] <tmp_dict[i] < tmp_dict[substitute]:
                            q.append([tmp_dict[i][0],tmp_dict[substitute][0]])
                           
                           # print(min(tmp_dict[ele])+1,min(tmp_dict[i])+1,min(tmp_dict[substitute])+1)
                            
        else:
            flag=2
            for i in range(-ele,1):
                if i in tmp_dict:
                    substitute = -(ele +i)
                    if substitute in tmp_dict:
                        if tmp_dict[ele] <tmp_dict[i] < tmp_dict[substitute]:
                            q.append([tmp_dict[i][0],tmp_dict[substitute][0]])
                            #print(min(tmp_dict[ele])+1,min(tmp_dict[i])+1,min(tmp_dict[substitute])+1)
        
        if q:
            #print(q,r)
            if flag ==1 :
                print("Negative Number")
            elif flag==2:
                print("Positive Number")
            data = min(q, key = lambda x:x[0])
            #x  print(data)
            print(min(tmp_dict[ele])+1,data[0]+1,data[1]+1) 
           
            return                     
        
        
    print(-1)
    return -1

if __name__ == "__main__":
    with open("/home/yannis/Downloads/rosalind_3sum(1).txt", "r") as f:
        k, n = map(int, f.readline().strip().split())
        A = [[int(i) for i in line.strip().split()] for line in f]
    for i in range(k):
        r = three_sum(A[i])