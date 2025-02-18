while True:
    n = int(input())
    if n == 0:
        break
    se = set()
    se.add(n)
    while n != 1:
        if n & 1 == 0:
            n >>= 1
        else:
            n = n * 3 + 1
        se.add(n)
    print(len(se))
