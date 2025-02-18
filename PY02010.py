def _sinusoid_():
    while True:
        n = int(input())
        if n == 0:
            break
        a = sorted([int(input()) for _ in range(n)])
        if a[0] == a[-1]:
            print("BANG NHAU")
        else:
            print(a[0], a[-1])

if __name__ == "__main__":
    _sinusoid_()