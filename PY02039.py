n = int(input())

a = []

for _ in range(n):
    a.append(list(map(int, input().split())))

sumUpper = sumLower = 0

for i in range(n):
    for j in range(n):
        if j > i:
            sumUpper += a[i][j]
        elif j < i:
            sumLower += a[i][j]

print("YES" if abs(sumUpper - sumLower) <= int(input()) else "NO")

print(abs(sumUpper - sumLower))