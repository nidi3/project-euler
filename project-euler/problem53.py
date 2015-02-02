from maths import factorial


def combination(n, r):
    return factorial(n) / factorial(r) / factorial(n - r)

s=0
for n in xrange(1,101):
    for r in xrange(1,101):
        if combination(n,r)>1000000: s+=1

print s