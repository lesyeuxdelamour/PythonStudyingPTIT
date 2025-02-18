def _sinusoid_():
    n, m = input().split()
    a = set((input().split()))
    b = set((input().split()))
    print("YES" if a == b else "NO")

if __name__ == "__main__":
    _sinusoid_()