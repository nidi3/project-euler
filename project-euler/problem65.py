from maths import cont_fraction
from strings import sum_digits

def c(n):
    return (1 + n / 3) * 2 if n % 3 == 1 else 1


print sum_digits(str(cont_fraction(100-1, 2, c)[0]))
