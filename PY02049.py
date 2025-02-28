def _sinusoid_():
    for _ in range(int(input())):
        n, p = map(int, input().split())
        cnt = 0;
        for i in range(p, n + 1, p):
            while i % p == 0:
                i //= p
                cnt += 1
        print(cnt)

if __name__ == "__main__":
    _sinusoid_()