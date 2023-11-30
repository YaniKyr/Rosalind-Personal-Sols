prob = [1,1,1,3/4,1/2,0]    #Offspring propability for the dominant genotype 
sample = [17411,18276,17353,16157,18485,19308]
count=0
for i in range(len(prob)):
    count+=(prob[i]*sample[i])*2

print(count)