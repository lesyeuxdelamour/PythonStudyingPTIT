def _sinusoid_():
    n = int(input())
    a = list(map(int, input().split()))
    res = max(a)
    l, r, curSum = 0, 0, 0
    for i in range(n):
        curSum += a[i]
        if curSum < 0:
            curSum = 0
            l = i + 1
        elif curSum > res:
            res = curSum
            r = i
    print(l + 1, r + 1, res)

if __name__ == "__main__":
    _sinusoid_()