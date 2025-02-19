from bisect import bisect_left

isPrime = [1] * 10001
primes = []

def sieve():
    isPrime[0] = isPrime[1] = 0
    for i in range(2, 10001):
        if isPrime[i] == 1:
            for j in range(i * i, 10001, i):
                isPrime[j] = 0
            primes.append(i)

def nearestPrime(n):
    idx = bisect_left(primes, n)
    left = primes[idx - 1] if idx > 0 else float("-inf")
    right = primes[idx] if idx < len(primes) else float("-inf")
    return min(abs(n - left), abs(n - right))

def _sinusoid_():
    sieve()
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    for i in a:
        if isPrime[i] == 0:
            res = max(res, nearestPrime(i))
    print(res)

if __name__ == "__main__":
    _sinusoid_()