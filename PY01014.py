a, k, n = map(int, input().split())

if (a // k + 1) * k >= n:
	print(-1)
else:
	for i in range(k - a % k, n - a + 1, k):
		print(i, end = ' ')
