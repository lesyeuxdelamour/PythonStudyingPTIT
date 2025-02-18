def _sinusoid_():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(*a[k:], *a[:k])

if __name__ == "__main__":
    _sinusoid_()