from Bio.Seq import Seq
from Bio import Entrez
from Bio import SeqIO

Entrez.email="kuriako1234@gmail.com"

formats = "NM_001079732 NM_204821 BT149870 NR_073358 JF927157 JX317645 JX460804 NM_001015511"

handle = Entrez.efetch(db="nucleotide", id=[formats], rettype="fasta")

records = list (SeqIO.parse(handle, "fasta"))

minimum = 10000000000000000000
best_min = None
for ele in records:
  sequence = ele.seq
  print(len(sequence))
  if len(sequence) < minimum:
    
    minimum = len(sequence)
    best_min = ele

minimum = 10000000000000000000
best_min = None
for ele in records:
  sequence = ele.seq
  print(len(sequence))
  if len(sequence) < minimum:
    
    minimum = len(sequence)
    best_min = ele

print(">",best_min.description,'\n',best_min.seq)
