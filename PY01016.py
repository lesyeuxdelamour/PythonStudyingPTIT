def decode(s):
	l = len(s)
	for i in range(1, l, 2):
		for j in range(int(s[i])):
			print(s[i - 1], end = '')
	print()

tc = int(input())

for _ in range(tc):
	s = input()
	decode(s)
