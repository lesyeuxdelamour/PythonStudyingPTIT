from math import isqrt

def sieve(n):
    divisor = [i for i in range(n + 1)]
    for i in range(2, isqrt(n) + 1):
        for j in range(i * i, n + 1, i):
            if divisor[j] == j:
                divisor[j] = i
    return divisor

n = int(input())

divisor = sieve(isqrt(n))

cnt = 0

for i in range(2, isqrt(n) + 1):
    p, q = divisor[i], divisor[i // divisor[i]]
    if divisor[i] == i:
        if i ** 8 <= n:
            cnt += 1
    elif p * q == i and p != q:
        cnt += 1

print(cnt)