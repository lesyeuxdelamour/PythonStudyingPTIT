n, m = map(int, input().split())

a, dd, d = [], [], [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

for _ in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            dd.append([i, j])

cnt = 0

for i in dd:
    for j in d:
        x, y = i[0] + j[0], i[1] + j[1]
        if 0 <= x < n and 0 <= y < m and a[x][y] != 0:
            cnt += a[x][y]
            a[x][y] = 0

print(cnt)