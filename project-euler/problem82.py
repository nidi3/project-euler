from strings import read_split
from maths import array

raw = read_split('p082_matrix.txt', '\n')
matrix = map(lambda line: map(lambda e: int(e), line.split(',')), raw)
d = 80
m = array(d, d)

for y in xrange(0, d):
    m[y][d - 1] = matrix[y][d - 1]

for x in xrange(d - 2, -1, -1):
    for ys in xrange(0, d):
        s = 100000000
        for ye in xrange(ys, d):
            t = 0
            for y in xrange(ys, ye + 1):
                t += matrix[y][x]
                if t + m[y][x + 1] < s: s = t + m[y][x + 1]
        for ye in xrange(ys, -1, -1):
            t = 0
            for y in xrange(ys, ye - 1, -1):
                t += matrix[y][x]
                if t + m[y][x + 1] < s: s = t + m[y][x + 1]
        m[ys][x] = s

l = 10000000
for y in xrange(0, d):
    if m[y][0] < l: l = m[y][0]
print l