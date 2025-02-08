from math import *

tc = int(input())

for _ in range(tc):
    n = input()
    if(gcd(int(n), int(n[::-1])) == 1):
        print("YES")
    else:
        print("NO")
