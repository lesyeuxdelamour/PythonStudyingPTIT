n = int(input())

a = map(int, input().split())
res = -int(1e9)

for i in a:
    res = max(res, i)

l = r = curSum = 0

for i in range(n):
    sum += a[i]
    if sum < 0:
        sum = 0
        l = i + 1
    elif sum > res:
        res = sum
        r = i

print(l + 1, r + 1, res)
