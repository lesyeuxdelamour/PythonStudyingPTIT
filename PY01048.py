def _sinusoid_():
    for _ in range(int(input())):
        n = int(input())
        cnt = 0
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                if i & 1 == 1:
                    cnt += 1
                if i * i != n and (n // i) & 1 == 1:
                    cnt += 1
        if n & 1 == 1:
            cnt += 1
        print(cnt)

if __name__ == "__main__":
    _sinusoid_()