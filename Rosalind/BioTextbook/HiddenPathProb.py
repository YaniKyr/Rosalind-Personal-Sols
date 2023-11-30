stringpi = "AABAAAAAAAABBBABBBBBBBAAAABBBABBAABBBBABAAAAABBBAA"
stringx =  "zxxxzyxxzxzzxxyyyyyyyyxzzyyzxzyxzzyyyzzyyxzzzzxzxy"
lexicon  = {'A':0,'B':1,'x':0,'y':1,'z':2}
trans_matrix = [[0.378,0.206,0.415],[0.424,0.371,0.204]]

def Prob(stringx,stringp):
    prob =1

    for count in range(len(stringx)):
        
        prob *=trans_matrix[lexicon[stringpi[count]]][lexicon[stringx[count]]]
print(prob)