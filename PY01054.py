def productDigit(n):
    pro = 1
    while n > 0:
        if n % 10 != 0:
            pro *= n % 10
        n //= 10
    return pro

tc = int(input())

for _ in range(tc):
    n = int(input())
    print(productDigit(n))