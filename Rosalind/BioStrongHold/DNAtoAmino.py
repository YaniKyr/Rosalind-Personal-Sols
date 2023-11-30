file = open("DNA.txt","r")
Dfile = file.read()

temp = Dfile.replace('\n',"")

def AntigraFh(Dna):
    i=0
    mRna = []*len(Dna)
    while(i!=len(Dna)):
        if(Dna[i] == 'A'): mRna.append('U')
        if(Dna[i] == 'G'): mRna.append('C')
        if(Dna[i] == 'T'): mRna.append('A')
        if(Dna[i] == 'C'): mRna.append('G')
        i+=1
    return mRna



def MRnatoAmino(GenCode,mRna):
    amino =[]
    all_amino = [[]]
    for i in range(len(mRna)):
        if(mRna[i] == 'A'):
            if(mRna[i+1] == 'U'):
                if(mRna[i+2] == 'G'):
                    for j in range(i,len(mRna),3 ):
                        if(j+1 >len(mRna) or j+2 > len(mRna) ):
                            return all_amino
                        else:
                            temp = mRna[j] +mRna[j+1] +mRna[j+2]
                            for key in GenCode.keys():
                                if(key == temp):
                                    if(GenCode[key] == 'STOP'):
                                        amino.append(GenCode[key])
                                        all_amino.append(amino)
                                    else: amino.append(GenCode[key])
                else: continue
            else: continue
        else: continue
    
    

GenCode = {'UUU':'PHE','UUC':'PHE','UUA':'LEU','UUG':'LEU','UCU':'SER',
           'UCC':'SER','UCA':'SER','UCG':'SER','UAU':'TYR','UAC':'TYR',
           'UAA':'STOP','UAG':'STOP','UGU':'CYS','UGC':'CYS','UGA':'STOP',
           'UGG':'TRP','CUU':'LEU','CUC':'LEU','CUA':'LEU','CUG':'LEU',
           'CCU':'PRO','CCC':'PRO','CCA':'PRO','CCG':'PRO','CAU':'HIS',
           'CAC':'HIS','CAA':'GLN','CAG':'GLN','CGU':'ARG','CGC':'ARG',
           'CGA':'ARG','CGG':'ARG','AUU':'ILE','AUC':'ILE','AUA':'ILE',
           'AUG':'MET','ACU':'THR','ACC':'THR','ACA':'THR','ACG':'THR',
           'AAU':'ASN','AAC':'ASN','AAA':'LYS','AAG':'LYS','AGU':'SER',
           'AGC':'SER','AGA':'ARG','AGG':'ARG','GUU':'VAL','GUC':'VAL',
           'GUA':'VAL','GUG':'VAL','GCU':'ALA','GCC':'ALA','GCA':'ALA',
           'GCG':'ALA','GAU':'ASP','GAC':'ASP','GAA':'GLU','GAG':'GLU',
           'GGU':'GLY','GGC':'GLY','GGA':'GLY','GGG':'GLY'}

mRna = AntigraFh(temp)

amino = MRnatoAmino(GenCode,mRna)

print(amino)