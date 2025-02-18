def _sinusoid_():
    n = int(input())
    a = list(map(int, input().split()))
    max1 = max2 = max3 = -1e4
    min1 = min2 = 1e4
    for i in a:
        if i > max1:
            max3, max2, max1 = max2, max1, i
        elif i > max2:
            max3, max2 = max2, i
        elif i > max3:
            max3 = i
        if i < min1:
            min2, min1 = min1, i
        elif i < min2:
            min2 = i
    print(max(max1 * max2 * max3, max1 * min1 * min2, max1 * max2))


if __name__ == "__main__":
    _sinusoid_()