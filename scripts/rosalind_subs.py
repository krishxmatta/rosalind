def find_motif(s, t):
    ret = []
    for i in range(len(s)):
        if(s[i:i + len(t)] == t):
            ret.append(i + 1)
    return ret

f = open("../data/rosalind_subs.txt", 'r')
s = f.readline().strip()
t = f.readline().strip()

ret = find_motif(s, t)
print(" ".join(str(i) for i in ret))
