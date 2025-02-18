def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1

def findMaxPrime(a):
    a.sort(reverse = True)
    for i in a:
        if isPrime(i):
            return i
    return -1

def _sinusoid_():
    n, m = map(int, input().split())
    a, tmp = [], []
    for _ in range(n):
        inp = list(map(int, input().split()))
        a.append(inp)
        tmp += inp
    x = findMaxPrime(tmp)
    if x == -1:
        print("NOT FOUND")
    else:
        print(x)
        for i in range(n):
            for j in range(m):
                if a[i][j] == x:
                    print(f"Vi tri [{i}][{j}]")   

if __name__ == "__main__":
    _sinusoid_()