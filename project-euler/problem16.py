from string import to_digit


def pow(a, n):
    s = 1
    while n > 0:
        if n % 2 == 1:
            s *= a
        n /= 2
        a *= a
    return s


print reduce(lambda accu, v: accu + to_digit(v), str(pow(2, 1000)), 0)

