def productDigit(n):
    pro = 1
    while n > 0:
        pro *= n % 10
        n //= 10
    return pro

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key = lambda x: (productDigit(x), x))
    print(*a)