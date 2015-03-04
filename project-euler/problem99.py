import math

from strings import read_split


lines = read_split('p099_base_exp.txt', '\n')

m = 0
n = 0
for line in lines:
    n += 1
    a, b = map(lambda x: int(x), line.split(','))
    v = math.exp(float(b) / 10000 * math.log(a))
    if v > m:
        m = v
        mn = n

print mn