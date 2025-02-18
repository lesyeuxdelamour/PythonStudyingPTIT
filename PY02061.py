for _ in range(int(input())):
    n, m = map(int, input().split())
    a = []
    k = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    for _ in range(3):
        k.append(list(map(int, input().split())))
    sum = 0
    for i in range(n - 2):
        for j in range(m - 2):
            for i1 in range(3):
                for j1 in range(3):
                    sum += a[i + i1][j + j1] * k[i1][j1]
    print(sum)