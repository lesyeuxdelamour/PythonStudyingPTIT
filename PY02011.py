def _sinusoid_():
    n = int(input())
    a = list(map(int, input().split()))
    sortedArr = sorted(a)
    if n & 1 == 0:
        median1 = sortedArr[n // 2]
        median2 = sortedArr[n // 2 - 1]
        median = median1 if a.index(median1) < a.index(median2) else median2
    else:
        median = sortedArr[n // 2]
    print(sum(abs(i - median) for i in a), median)

if __name__ == "__main__":
    _sinusoid_()
