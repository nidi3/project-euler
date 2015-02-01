f1 = 1
f2 = 1
i = 1
limit = pow(10, 1000 - 1)
while f2 < limit:
    i += 1
    f1, f2 = f1 + f2, f1

print i