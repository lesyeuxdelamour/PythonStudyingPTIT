def _sinusoid_():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        res = 0
        for i in a:
            res ^= i
        print(res)

if __name__ == "__main__":
    _sinusoid_()