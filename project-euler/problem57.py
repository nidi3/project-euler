from cont_frac import eval_cont_frac


def c(n): return 1 if n == 0 else 2


s = 0
for n in xrange(1, 1001):
    d = eval_cont_frac(n, c)
    if len(str(d[0])) > len(str(d[1])):
        s += 1

print s