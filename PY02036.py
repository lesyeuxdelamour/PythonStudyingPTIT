from math import gcd

n = int(input())

a = list(map(int, input().split()))

a.sort()

for i in a:
    for j in a:
        if i < j and gcd(i, j) == 1:
            print(i, j, sep = ' ')