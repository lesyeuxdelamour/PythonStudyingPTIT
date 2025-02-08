from math import *

tc = int(input())

for _ in range(tc):
    n = int(input())
    print(1, end = " * ")
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                n //= i
                cnt += 1
            print(i, cnt, sep = "^", end = '')
            if n != 1:
                print(" * ", end = '')
    if n != 1:
        print(n, 1, sep = "^", end = '')
    print()