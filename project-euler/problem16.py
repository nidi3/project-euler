from strings import sum_digits


def pow(a, n):
    s = 1
    while n > 0:
        if n % 2 == 1:
            s *= a
        n /= 2
        a *= a
    return s


print sum_digits(str(pow(2, 1000)))

