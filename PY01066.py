def check(s):
    sT = s[::-1]
    l = len(s)
    for i in range(l - 1):
        if abs(ord(s[i + 1]) - ord(s[i])) != abs(ord(sT[i + 1]) - ord(sT[i])):
            return "NO"
    return "YES"

for _ in range(int(input())):
    s = input()
    print(check(s))