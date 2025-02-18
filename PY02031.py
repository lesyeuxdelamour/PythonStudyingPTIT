from math import isqrt

def isPrime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

n, m = map(int, input().split())

a = []

for _ in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        print(1 if isPrime(a[i][j]) else 0, end = ' ')
    print() 