def check(s):
    sT = s[::-1]
    l = len(s)
    for i in range(l - 1):
        if abs(ord(s[i + 1]) - ord(s[i])) != abs(ord(sT[i + 1]) - ord(sT[i])):
            return False
    return True

tc = int(input())

for _ in range(tc):
    s = input()
    if(check(s)):
        print("YES")
    else:
        print("NO")