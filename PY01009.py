s = input()

upper = 0

for c in s:
	if c.isupper():
		upper += 1

lower = len(s) - upper

if upper > lower:
	print(s.upper())
else:
	print(s.lower())