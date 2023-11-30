import numpy as np
from Bio import SeqIO
from operator import itemgetter
from itertools import groupby
def findMotif(a,b,k=0):
    
    best_motif=[]
    ranges = []
    while(k+len(b)<=len(a)):  
        new=[]  
        for i,j in zip(a[k:],b):
            new.append(ord(i)^ord(j))
        x = np.array(new)
        
        indexes  = np.where(x==0)[0]
        print(indexes)
        for m,n in groupby(enumerate(indexes),lambda l:l[0]-l[1]):
            group = map(itemgetter(1), n)
            group = list(map(int,group))
            ranges.append((group[0],group[-1]))

        #print("Here",ranges)
        k+=1
    return ranges
    
    
    
    
        
nlist = []
for record in SeqIO.parse("DNA.txt","fasta"):
   
    nlist.append(record)
print(nlist[0].seq)

seq_max = max(nlist, key=lambda x:x.seq)
seq_min = min(nlist, key=lambda x:x.seq)



motifs = findMotif(seq_max,seq_min,0)
print(motifs)
for ele in nlist:
    if ele.seq == seq_max.seq or ele.seq == seq_min.seq:
        continue
    for motif in motifs:
        
        print(motif)
        k=0
        while(k+len(seq_min)<=len(ele)+1):
            #print("\n\n\nTrying:",ele.seq[k:len(motif)+k] , seq_min.seq[motif[0]:motif[-1]])
            if ele.seq[k:len(motif)+k] == seq_min.seq[motif[0]:motif[-1]+1]:
                
                print(seq_min.seq[motif[0]-1:motif[-1]])
                print("success")
            k+=1

#TO DO:
#See Why it does not get all the values the ele and seq_min