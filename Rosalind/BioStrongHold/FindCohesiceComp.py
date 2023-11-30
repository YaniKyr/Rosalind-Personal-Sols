import DDArray as dd
structure,temp = dd.Make_Graph("sample.txt",1)

f = open("output.txt","w")


for ele in temp:
    print(ele,end=" ")
    f.write(f'{ele} ')
print("\n")

dd.FindCost()