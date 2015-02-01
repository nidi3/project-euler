def to_digit(s): return ord(s) - ord('0')


def read_matrix(s):
    g = []
    for line in s.split('\n'):
        g.append(map(lambda x: int(x), line.split(' ')))
    return g


def sum_digits(s): return reduce(lambda accu, v: accu + to_digit(v), s, 0)
