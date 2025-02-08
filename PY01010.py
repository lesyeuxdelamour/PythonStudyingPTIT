tc = int(input())

for _ in range(tc):
	n = input()
	first = n[:2]
	last = n[-2:]
	if first == last:
		print("YES")
	else:
		print("NO")
