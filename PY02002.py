fibo = [0, 1, 1]

for i in range(3, 93):
    fibo.append(fibo[i - 1] + fibo[i - 2])

for _ in range(int(input())):
    l, r = map(int, input().split())
    for i in range(l, r + 1):
        print(fibo[i], end = ' ')
    print()