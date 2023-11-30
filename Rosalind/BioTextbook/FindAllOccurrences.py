from operator import index


def FindP(text,pattern):
    indexes =[]
    
    for j,ele in enumerate(text):

        
        
        if text[j:j+len(pattern)] == pattern:
            
           indexes.append(j)
    for ele in indexes:   
        print(ele,end=" ")
text = "CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC"
FindP(text,"AGACGTGAG")
