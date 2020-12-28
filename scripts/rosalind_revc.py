def gen_revc(seq):
    complement = {
        'A':'t',
        'T':'a',
        'C':'g',
        'G':'c',
    }

    for key, value in complement.items():
        seq = seq.replace(key, value)

    return seq.upper()[::-1]

f = open("../data/rosalind_revc.txt")
seq = f.read().strip()

ret = gen_revc(seq)
print(ret)
