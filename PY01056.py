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

def check(n):
    for i in range(len(n)):
        if i & 1 != int(n[i]) & 1:
            return False
    return isPrime(sumDigit(int(n)))

tc = int(input())

for _ in range(tc):
    n = input()
    if(check(n)):
        print("YES")
    else:
        print("NO")
    print(2 % 0)