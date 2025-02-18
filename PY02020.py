n = int(input())

a = list(map(float, input().split()))

a.sort()

res = 0.0
cnt = 0

for i in a:
    if i != a[0] and i != a[n - 1]:
        res += i
        cnt += 1

print(f"{res / cnt:.2f}")