def _sinusoid_():
    while True:
        n = int(input())
        if n == -1:
            break
        print(n if n % 9 == 0 else (n // 9 + 1) * 9)

if __name__ == "__main__":
    _sinusoid_()