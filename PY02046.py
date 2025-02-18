def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1

def check(a, n):
    if n < 2:
        return "NOT FOUND"
    se = set()
    prefixSum = []
    for i in range(n):
        if a[i] not in se:
            se.add(a[i])
            prefixSum.append(a[i])
    m = len(prefixSum)
    if m < 2:
        return "NOT FOUND"
    for i in range(1, m):
        prefixSum[i] += prefixSum[i - 1]
    for i in range(0, m):
        if isPrime(prefixSum[i]) and isPrime(prefixSum[m - 1] - prefixSum[i]):
            return str(i)
    return "NOT FOUND"

def _sinusoid_():
    n = int(input())
    a = list(map(int, input().split()))
    print(check(a, n))

if __name__ == "__main__":
    _sinusoid_()    