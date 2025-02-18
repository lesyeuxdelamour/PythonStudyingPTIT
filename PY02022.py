isPrime = [1] * 1000001

def sieve():
    isPrime[0] = isPrime[1] = 0
    for i in range(2, 1001):
        if isPrime[i] == 1:
            for j in range(i * i, 1000001, i):
                isPrime[j] = 0

sieve()

n = int(input())

a = list(map(int, input().split()))

mp = {}

for i in a:
    if isPrime[i]:
        mp[i] = mp.get(i, 0) + 1

for i in mp:
    print(i, mp[i], sep = ' ')  