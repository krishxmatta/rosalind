def fib(n, k):
    if(n <= 2):
        return 1
    return fib(n - 1, k) + (k * fib(n - 2, k))

f = open("../data/rosalind_fib.txt", 'r')
n, k = [int(i) for i in f.read().strip().split(' ')]

ret = fib(n, k)
print(ret)
