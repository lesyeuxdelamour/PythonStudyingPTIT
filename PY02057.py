def _sinusoid_():
    n, m = map(int, input().split())
    a, tmp = [], []
    for _ in range(n):
        inp = list(map(int, input().split()))
        a.append(inp)
        tmp += inp
    tmp.sort()
    x = tmp[-1] - tmp[0]
    if x not in tmp:
        print("NOT FOUND")
    else:
        print(x)
        for i in range(n):
            for j in range(m):
                if a[i][j] == x:
                    print(f"Vi tri [{i}][{j}]")   

if __name__ == "__main__":
    _sinusoid_()