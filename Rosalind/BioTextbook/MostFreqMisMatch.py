#NOT DONE


def FindP(text,size):
    indexes =[]
    patterns = []
    for j in range(len(text)-size):
        patterns.append(text[j:])
        missmatch =0 
        for i in range(size):
            if text[i+j] != pattern[i]:
                missmatch+=1
        if missmatch<=5:
            indexes.append(j)

    for ele in indexes:
        print(ele, end=" ")
        
text = ""
FindP(text,"ATTCGTGAGACC")
