from math import *

def sumDigit(n):
	res = 0
	while n > 0:
		res += n % 10
		n //= 10
	return res

def isPrime(n):
	for i in range(2, int(sqrt(n).real) + 1):
		if n % i == 0:
			return False
	return n > 1

tc = int(input())

for _ in range(tc):
	a, b = map(int, input().split())
	if isPrime(sumDigit(gcd(a, n))):
		print("YES")
	else:
		print("NO")
