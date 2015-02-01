def to_digit(s, zero='0'): return ord(s) - ord(zero)


def read_matrix(s):
    g = []
    for line in s.split('\n'):
        g.append(map(lambda x: int(x), line.split(' ')))
    return g


def sum_digits(s): return reduce(lambda accu, v: accu + to_digit(v), s, 0)


def is_palindrom(n):
    s = str(n)
    return s == s[::-1]

def digits_of(n):
    d = [0] * 10
    s = str(n)
    for c in s:
        d[to_digit(c)] += 1
    return d
