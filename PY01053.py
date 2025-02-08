def sumDigit(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

tc = int(input())

for _ in range(tc):
    n = int(input())
    if(sumDigit(n) % 3 == 0):
        print("YES")
    else:
        print("NO")