def check(n):
	for i in n:
		if int(i) & 1 == 1:
			return False
	return True

a = []
num = 2

while num <= 888:
	if check(str(num)):
		tmp = str(num)
		a.append(int(tmp + tmp[::-1]))
	num += 2 

tc = int(input())

for _ in range(tc):
	n = int(input())
	for i in a:
		if i >= n:
			break
		print(i, end = ' ')
	print()
