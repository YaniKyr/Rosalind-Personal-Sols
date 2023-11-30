from Bio import SeqIO
n=26
sum =0
count = 0
record = list(SeqIO.parse("sample.txt","fastq"))
for ele in record:
    for index in ele.letter_annotations["phred_quality"]:
        print(index)
        if index <n :
            count+=1

print(count)
