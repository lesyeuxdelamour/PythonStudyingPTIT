def isIP(a):
	if len(a) != 4:
		return "NO"
	for i in a:
		if i < 0 or i > 255:
			return "NO"
	return "YES"

for _ in range(int(input())):
	try:
	    print(isIP(list(map(int, input().split(".")))))
	except:
	    print("NO")