isPrime = [1] * 100001
primes = [0]

def sieve():
    isPrime[0] = isPrime[1] = 0
    for i in range(2, 10001):
        if isPrime[i] == 1:
            for j in range(i * i, 10001, i):
                isPrime[j] = 0
            primes.append(i)

sieve()

n, x = map(int, input().split())

for i in range(0, n + 1):
    x = x + primes[i]
    print(x, end = ' ')


