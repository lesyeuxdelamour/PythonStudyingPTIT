def productDigit(n):
    pro = 1
    for i in range(0, len(n), 2):
        if n[i] != '0':
            pro *= int(n[i])
    return pro

def sumDigit(n):
    sum = 0
    for i in range(1, len(n), 2):
        sum += int(n[i])
    return sum

tc = int(input())

for _ in range(tc):
    n = input()
    print(productDigit(n), sumDigit(n))