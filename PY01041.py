def check(n):
    l = len(n)
    if l < 3:
        return False
    peak = -1
    for i in range(l - 1):
        if n[i] >= n[i + 1]:
            peak = i
            break
    if peak == -1 or peak == 0:
        return False
    for i in range(peak, l - 1):
        if n[i] < n[i + 1]:
            return False 
    return True

tc = int(input())

for _ in range(tc):
    n = input()
    if(check(n)):
        print("YES")
    else:
        print("NO")