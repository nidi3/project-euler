from strings import read_split
from maths import array

raw = read_split('p081_matrix.txt', '\n')
matrix = map(lambda line: map(lambda e: int(e), line.split(',')), raw)
m = array(80,80)

m[79][79] = matrix[79][79]
for s in xrange(78, -1, -1):
    m[s][79] = matrix[s][79] + m[s + 1][79]
    for x in xrange(78, s, -1):
        m[s][x] = matrix[s][x] + min(m[s][x + 1], m[s + 1][x])

    m[79][s] = matrix[79][s] + m[79][s + 1]
    for y in xrange(78, s, -1):
        m[y][s] = matrix[y][s] + min(m[y + 1][s], m[y][s + 1])

    m[s][s] = matrix[s][s] + min(m[s][s + 1], m[s + 1][s])

print m[0][0]
