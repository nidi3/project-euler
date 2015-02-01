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
