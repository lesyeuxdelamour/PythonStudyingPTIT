def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1

def check(n):
    curSum, tmp = 0, n
    while n > 0:
        if not isPrime(n % 10):
            return "No"
        curSum += n % 10
        n //= 10
    return "Yes" if isPrime(curSum) and isPrime(tmp) and isPrime(int(str(tmp)[::-1])) else "No"

def _sinusoid_():
    for _ in range(int(input())):
        print(check(int(input())))

if __name__ == "__main__":
    _sinusoid_()