from math import *

# Hàm phi Euler
def totient(n): 
	res = n
	for p in range(2, int(sqrt(n)) + 1):
		if n % p == 0:
			while n % p == 0:
				n //= p
			res -= res // p
	if n > 1:
		res -= res // n
	return res

def isPrime(n):
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False
	return n > 1

tc = int(input())

for _ in range(tc):
	n = int(input())
	cnt = totient(n)
	if isPrime(cnt):
		print("YES")
	else:
		print("NO")