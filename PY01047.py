from math import *

def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

tc = int(input())

for _ in range(tc):
    s = input()
    if isPrime(int(s[-4:])):
        print("YES")
    else:
        print("NO")