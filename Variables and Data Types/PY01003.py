def makeRound(n):
	mul = 10;
	while n // mul > 0:
		if n % mul >= mul // 2:
			n = (n // mul + 1) * mul
		else:
			n = (n // mul) * mul
		mul *= 10
	mul //= 10
	return n // mul * mul

tc = int(input())

for _ in range(tc):
	n = int(input())
	print(makeRound(n))	