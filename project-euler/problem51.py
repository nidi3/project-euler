from primes import is_prime
from maths import choose, to_list, to_num


def replace(length, z, s):
    zl = [0] * (z + s)
    for x in xrange(10 ** (z - 1) + 1, 10 ** z, 2):
        xl = to_list(x)
        for c in choose(s, z + s - 1):
            q = 0
            for p in xrange(0, len(zl)):
                if p not in c:
                    zl[p] = xl[q]
                    q += 1
            ps = 0
            first = 0
            for k in xrange(9, -1, -1):
                for p in c:
                    zl[p] = k
                zz = to_num(zl)
                if zl[0] != 0 and is_prime(zz):
                    first = zz
                else:
                    ps += 1
                    if ps == 11 - length: break

            if ps == 10 - length:
                print first


replace(8, 3, 2)
replace(8, 3, 3)
