isPrime = [1] * 1001

def sieve():
    isPrime[0] = isPrime[1] = 0
    for i in range(2, 32):
        if isPrime[i] == 1:
            for j in range(i * i, 1001, i):
                isPrime[j] = 0

def _sinusoid_():
    sieve()
    n = int(input())
    a = list(map(int, input().split()))
    prime = sorted(i for i in a if isPrime[i])
    idx = 0
    for i in a:
        if isPrime[i] == 1:
            print(prime[idx], end = ' ')
            idx += 1
        else:
            print(i, end = ' ')

if __name__ == "__main__":
    _sinusoid_()