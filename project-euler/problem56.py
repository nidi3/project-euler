from strings import sum_digits

m = 0
for a in xrange(1, 100):
    for b in xrange(1, 100):
        s = sum_digits(str(pow(a, b)))
        if s > m: m = s

print m