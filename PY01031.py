digits = [str(i) for i in range(10)] + [chr(c) for c in range(ord('A'), ord('Z') + 1)]

for _ in range(int(input())):
    n, m = map(int, input().split())
    res = ""
    while n > 0:
        res += digits[n % m]
        n //= m
    print(res[::-1])    