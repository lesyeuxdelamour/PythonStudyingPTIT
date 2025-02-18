def sumDigit(n):
    sum = 0
    for i in range(0, len(n), 2):
        sum += int(n[i])
    return sum

def productDigit(n):
    pro, flag = 1, 0
    for i in range(1, len(n), 2):
        if n[i] != '0':
            flag = 1
            pro *= int(n[i])
    return pro if flag == 1 else 0  

tc = int(input())

for _ in range(tc):
    n = input()
    print(sumDigit(n), productDigit(n))