n = int(input())

sum = n * (n + 1) // 2

for _ in range(n - 1):
	x = int(input())
	sum -= x

print(sum)