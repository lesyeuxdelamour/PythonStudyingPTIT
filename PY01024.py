def check(n):
    sum = int(n[0])
    l = len(n)
    for i in range(l - 1):
        if abs(int(n[i + 1]) - int(n[i])) != 2:
            return False
        sum += int(n[i + 1])
    if sum % 10 != 0:
        return False
    return True

tc = int(input())

for _ in range(tc):
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")