tc = int(input())

for _ in range(tc):
    n = int(input())
    res = 0.0
    if n & 1 == 1:
        for i in range(1, n + 1, 2):
            res += 1 / i
    else:
        for i in range(2, n + 1, 2):
            res += 1 / i
    print(f"{res:.6f}") 