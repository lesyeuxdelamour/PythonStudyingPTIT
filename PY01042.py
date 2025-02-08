def check(s):
    for i in s:
        if i != '0' and i != '1' and i != '2':
            return False
    return True

tc = int(input())

for _ in range(tc):
    s = input()
    if(check(s)):
        print("YES")
    else:
        print("NO")