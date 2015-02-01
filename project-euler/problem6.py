def sum(n, f):
    s = 0
    for n in xrange(1, n + 1):
        s += f(n)
    return s


sum_squares = sum(100, lambda n: n * n)
sum = sum(100, lambda n: n)

print sum * sum - sum_squares