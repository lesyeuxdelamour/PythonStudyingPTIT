def accumulateDigit(n):
    acc = 1
    while n > 0:
        if n % 10 != 0:
            acc *= n % 10
        n //= 10
    return acc

tc = int(input())

for _ in range(tc):
    n = int(input())
    print(accumulateDigit(n))