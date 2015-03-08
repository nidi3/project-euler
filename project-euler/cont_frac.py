def eval_cont_frac(n, coeff):
    a = 1
    b = coeff(n)
    for x in xrange(n - 1, 0, -1):
        a, b = b, a + coeff(x) * b
    return [a + coeff(0) * b, b]


def cont_frac_of_root(q):
    from math import floor, sqrt

    s = set()
    r = sqrt(q)
    a = 1
    b = floor(r)
    l = [int(b)]
    if b != r:
        while (a, b) not in s:
            s.add((a, b))
            a, b = b, (q - b * b) / a
            n = floor((r + a) / b)
            l.append(int(n))
            a, b = b, n * b - a

    return l


def coeff_from_periodic(coeffs):
    def coeff(n):
        return coeffs[0] if n == 0 else coeffs[(n - 1) % (len(coeffs) - 1) + 1]

    return coeff
