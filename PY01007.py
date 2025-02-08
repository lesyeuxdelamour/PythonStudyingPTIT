from math import *

tc = int(input())

for _ in range(tc):
	n, x, m = list(map(float, input().split()))
	x /= 100
	res = log(m / n, 1 + x)
	print(ceil(res))
