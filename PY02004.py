n = int(input())

a = list(map(int, input().split()))

cnt = 0

for i in range(1, n):
    cnt += a[i - 1] ^ a[i]

print(cnt)