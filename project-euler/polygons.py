from math import sqrt, floor, fabs


def is_trigonal(n):
    s = (-.5 + sqrt(.25 + 2 * n))
    return fabs(s - floor(s)) < .00001


def is_square(n):
    s = sqrt(n)
    return fabs(s - floor(s)) < .00001


def is_pentagonal(n):
    s = (.5 + sqrt(.25 + 6 * n)) / 3
    return fabs(s - floor(s)) < .00001


def is_hexagonal(n):
    s = (1 + sqrt(1 + 8 * n)) / 4
    return fabs(s - floor(s)) < .00001


def is_heptagonal(n):
    s = (1.5 + sqrt(2.25 + 10 * n)) / 5
    return fabs(s - floor(s)) < .00001


def is_octagonal(n):
    s = (2 + sqrt(4 + 12 * n)) / 6
    return fabs(s - floor(s)) < .00001


def pentagonal(n): return n * (3 * n - 1) / 2


def octagonal(n): return n * (3 * n - 2)


def trigonal_gen(n):
    while True:
        yield n * (n + 1) / 2
        n += 1


def pentagonal_gen(n):
    while True:
        yield n * (3 * n - 1) / 2
        n += 1


def hexagonal_gen(n):
    while True:
        yield n * (2 * n - 1)
        n += 1

