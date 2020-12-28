def transcribe_rna(seq):
    return seq.replace('T', 'U')

f = open("../data/rosalind_rna.txt", 'r')
seq = f.read().strip()

ret = transcribe_rna(seq)
print(ret)
