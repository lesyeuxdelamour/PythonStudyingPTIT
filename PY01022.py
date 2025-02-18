def sumDigit(n):
    sum = 0
    for i in n:
        sum += ord(i) - ord('0')
    return sum

n = input()

cnt = 0

while len(n) > 1:
    n = str(sumDigit(n))
    cnt += 1

print(cnt)