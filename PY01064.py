def Try(n, k):
    if k < 2 ** (n - 1):
        return Try(n - 1, k)
    elif k > 2 ** (n - 1):
        return Try(n - 1, k - 2 ** (n - 1))
    return chr(ord('A') + n - 1)

for _ in range(int(input())):
    n, k = map(int, input().split())
    print(Try(n, k))
