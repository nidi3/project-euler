from strings import to_digit
from maths import factorial


m = 0
for n in xrange(3, 7 * factorial(9)):
    s = 0
    for c in str(n): s += factorial(to_digit(c))
    if s == n: m += s

print m
