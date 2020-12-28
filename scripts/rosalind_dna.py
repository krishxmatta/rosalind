def count_bases(seq):
  base_count = {
    'A': seq.count('A'),
    'C': seq.count('C'),
    'G': seq.count('G'),
    'T': seq.count('T'),
  }
  return base_count

f = open("../data/rosalind_dna.txt", 'r')
seq = f.read().strip()

base_count = count_bases(seq)

ret = ' '.join(str(value) for value in base_count.values())
print(ret)
