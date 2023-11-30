#Finding a Shared Motif
class Rosalinds:
    def __init__(self,DNA):
        self.DNA = DNA
        self.motifs = []



data='''
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA'''



import re 
dat  =data.split()
print(dat)
status = 0
i=0
step=2
array = []
sequences = [] 
for i in range(1,len(dat),2):
    array.append(Rosalinds(dat[i]))
    sequences.append([])

while status !=1:
    seq = array[0].DNA[i:i+step]
    for k in range(1,len(array)-1):
        for j in range(i,len(array)):
            array[k].motifs.append(re.search(seq,array[j][i:i+step]))
    
    
    i+=1
    
    if i>=len(dat[1]):
        status=1

for seq in sequence1:
    if seq is None: continue   
    print(seq.group())