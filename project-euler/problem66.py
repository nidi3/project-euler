from cont_frac import cont_frac_of_root, eval_cont_frac, coeff_from_periodic

q = set()
for x in xrange(1, 100000): q.add(x * x)


def min_solution(d):
    r = cont_frac_of_root(d)
    n = 0
    while True:
        p = eval_cont_frac(n, coeff_from_periodic(r))
        if p[0] * p[0] - d * p[1] * p[1] == 1:
            return p[0]
        n += 1


mx = md = 0
for d in xrange(1, 1001):
    if d not in q:
        x = min_solution(d)
        if x > mx:
            mx = x
            md = d

print md

