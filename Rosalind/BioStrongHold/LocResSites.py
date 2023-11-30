def Reverse_Comp(seq):
    dict = {'A':'T','T':'A','G':'C','C':'G'}
    list = []
    for i in range(len(seq)-1,-1,-1):
        list.append(dict[seq[i]])
    return list

def RPalindrome(string):
    list = []
    sz=4
    i=0
    temp = []

    while i != len(string):
        for sz in range(4,13):
            
            seq = ""
            
            if i+sz> len(string): break
            seq = seq.join( Reverse_Comp(string[i:i+sz]))
           
            if string[i:i+sz] == seq:
                temp = []
                
                temp = [i+1,sz]
                list.append(temp)
            
                
        i+=1
    return list

    
str = "TCAATGCATGCGGGTCTATATGCAT"

list = RPalindrome(str)
for li in list:
    print(li[0],li[1])