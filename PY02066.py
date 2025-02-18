def _sinusoid_():
    n = int(input())
    se = set()
    while len(se) < n:
        se.update(map(int, input().split()))
    if len(se) == max(se):
        print("Excellent!")
    else:
        for i in range(1, max(se)):
            if i not in se:
                print(i)

if __name__ == "__main__":
    _sinusoid_()