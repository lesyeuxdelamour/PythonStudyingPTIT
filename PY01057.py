from math import *

def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

def isValid(i, n):
    if isPrime(i):
        return n == '2' or n == '3' or n == '5' or n == '7'
    return n != '2' and n != '3' and n != '5' and n != '7'

def check(n):
    for i in range(len(n)):
        if not isValid(i, n[i]):
            return False
    return True

tc = int(input())

for _ in range(tc):
    n = input()
    if(check(n)):
        print("YES")
    else:
        print("NO")