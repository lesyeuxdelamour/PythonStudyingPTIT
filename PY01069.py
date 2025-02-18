def Try(s, n, a, b, c, d):
    if len(s) == n:
        if s[-1] != '2' and a > 0 and b > 0 and c > 0 and d > 0:
            print(s)
        return
    Try(s + "2", n, a + 1, b, c, d)
    Try(s + "3", n, a, b + 1, c, d)
    Try(s + "5", n, a, b, c + 1, d)
    Try(s + "7", n, a, b, c, d + 1)

def _sinusoid_():
    for i in range(4, int(input()) + 1):
        Try("", i, 0, 0, 0, 0)

if __name__ == "__main__":
    _sinusoid_()
