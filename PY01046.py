def Try(n, a, b, c):
    if n == 1:
        print(a, c, sep = " -> ")
        return
    Try(n - 1, a, c, b)
    Try(1, a, b, c)
    Try(n - 1, b, a, c)

n = int(input())

Try(n, 'A', 'B', 'C')