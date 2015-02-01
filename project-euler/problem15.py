from maths import array

s = array(21, 21)
s[1][0] = 1
s[0][1] = 1
s[1][1] = 2

for d in xrange(2, 21):
    s[0][d] = s[0][d - 1]
    s[d][0] = s[d - 1][0]
    for n in xrange(1, d):
        s[n][d] = s[n][d - 1] + s[n - 1][d]
        s[d][n] = s[d - 1][n] + s[d][n - 1]
    s[d][d] = s[d - 1][d] + s[d][d - 1]

print s[20][20]