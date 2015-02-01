from strings import sum_digits


def fac(n):
    f = 1
    for i in xrange(2, n + 1): f *= i
    return f


print sum_digits(str(fac(100)))