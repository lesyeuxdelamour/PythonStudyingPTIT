def _sinusoid_():
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    k = abs(n - m)
    if n > m:
        se = set()
        for i in range(0, 2 * k, 2):
            se.add(i)
        for i in range(n):
            if i not in se:
                for j in range(m):
                    print(a[i][j], end = ' ')
                print()

    elif m > n:
        se = set()
        for i in range(0, 2 * k, 2):
            se.add(i + 1)
        for i in range(n):
            for j in range(m):
                if j not in se:
                    print(a[i][j], end = ' ')
            print()
    else:
        for i in range(n):
            for j in range(m):
                print(a[i][j], end = ' ')
            print()

if __name__ == "__main__":
    _sinusoid_()