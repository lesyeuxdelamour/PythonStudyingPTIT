visited = set()
cnt = 0

def Try(idx, total, sub, x, a, n):
    global cnt
    if total > x:
        return 
    if sub == 2:
        cnt += 1
        return
    if total == x:
        Try(0, 0, sub + 1, x, a, n)
        return 
    for i in range(idx, n):
        if i not in visited:
            visited.add(i)
            Try(i + 1, total + a[i], sub, x, a, n)
            visited.remove(i)
            
# TLE
def _sinusoid_():
    global cnt
    for _ in range(int(input())):
        n = int(input())
        a = sorted(map(int, input().split()))
        total = sum(a)
        if total % 3 != 0:
            print(0)
            continue
        visited.clear()
        cnt = 0
        Try(0, 0, 0, total // 3, a, n)
        print(cnt)

if __name__ == "__main__":
    _sinusoid_()