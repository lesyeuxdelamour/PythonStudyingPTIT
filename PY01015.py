def check(n):
	l = len(n)
	for i in range(1, l):
		if n[i] < n[i - 1]:
			return False
	return True

tc = int(input())

for _ in range(tc):
	n = input()
	if(check(n)):
		print("YES")
	else:
		print("NO")
