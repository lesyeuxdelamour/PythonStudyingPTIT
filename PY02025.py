def _sinusoid_():
    n, m = input().split()
    a = set((input().split()))
    b = set((input().split()))
    print(*sorted(a & b))
    print(*sorted(a - b))
    print(*sorted(b - a))

if __name__ == "__main__":
    _sinusoid_()