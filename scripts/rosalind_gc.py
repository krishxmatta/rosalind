def fasta_parser(f):
    seq_list = {}
    line = f.readline().strip()
    while line:
        curr_seq = line[1:]
        seq_list[curr_seq] = ""
        line = f.readline().strip()
        while line and line[0] != '>':
            seq_list[curr_seq] += line
            line = f.readline().strip()
    return seq_list

def calculate_max_gc(seq_list):
    max_gc = 0
    opt_seq = ""
    for name, seq in seq_list.items():
        curr_gc = (seq.count('G') + seq.count('C')) / len(seq)
        if curr_gc > max_gc:
            max_gc = curr_gc
            opt_seq = name
    return opt_seq, max_gc


f = open("../data/rosalind_gc.txt", 'r')

opt_seq, max_gc = calculate_max_gc(fasta_parser(f))
print(opt_seq)
print(100 * max_gc)
