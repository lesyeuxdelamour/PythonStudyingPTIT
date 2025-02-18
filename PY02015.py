while True:
    a = list(map(int, input().split()))
    if a == [0, 0, 0, 0]:
        break
    cnt = 0
    while len(set(a)) > 1:
        tmp = []
        for i in range(1, 4):
            tmp.append(abs(a[i] - a[i - 1]))
        tmp.append(abs(a[3] - a[0]))
        a = tmp
        cnt += 1
    print(cnt)
