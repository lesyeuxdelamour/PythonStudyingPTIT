def sumDigit(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

def isPalindrome(s):
    return len(s) > 1 and s == s[::-1]

tc = int(input())

for _ in range(tc):
    n = int(input())
    if(isPrime(sumDigit(n))):
        print("YES")
    else:
        print("NO")