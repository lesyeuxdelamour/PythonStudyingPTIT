from math import *

def sumDigit(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

tc = int(input())

for _ in range(tc):
    n = int(input())
    if(isPrime(sumDigit(n))):
        print("YES")
    else:
        print("NO")