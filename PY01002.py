left, right = input().split('=')

if(eval(left) == eval(right)):
	print("YES")
else:
	print("NO")