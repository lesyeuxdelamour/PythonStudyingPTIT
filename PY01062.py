from math import *

def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

def check(n):
    if not isPrime(len(n)):
        return False
    cnt = 0
    for i in n:
        if isPrime(int(i)):
            cnt += 1
    return cnt > len(n) - cnt

tc = int(input())

for _ in range(tc):
    n = input()
    if(check(n)):
        print("YES")
    else:
        print("NO")