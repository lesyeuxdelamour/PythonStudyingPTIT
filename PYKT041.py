def _sinusoid_():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(input()))
    cnt = 0
    for i in range(n):
        row, col = 0, 0
        for j in range(n):
            if a[i][j] == 'C':
                row += 1
            if a[j][i] == 'C':
                col += 1
        cnt += row * (row - 1) // 2 + col * (col - 1) // 2
    print(cnt)

if __name__ == "__main__":
    _sinusoid_()