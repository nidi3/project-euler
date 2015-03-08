from cont_frac import cont_frac_of_root

t = 0
for n in xrange(2, 10001):
    if len(cont_frac_of_root(n)) % 2 == 0: t += 1

print t