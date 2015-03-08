from cont_frac import eval_cont_frac
from strings import sum_digits


def c(n):
    if n == 0:
        return 2
    if n % 3 == 2:
        return (1 + n / 3) * 2
    return 1


print sum_digits(str(eval_cont_frac(100 - 1, c)[0]))
