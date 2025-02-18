emirp = []

isPrime = [1] * 1000001

def pre():
    
    isPrime[0] = isPrime[1] = 0
    for i in range(2, 1001):
        if isPrime[i] == 1:
            for j in range(i * i, 1000001, i):
                isPrime[j] = 0
    # for i in range(13, 1000001):
    #     iT = int(str(i)[::-1])
    #     if i != iT and isPrime[i] and isPrime[iT]:
    #         emirp.append([i, iT])
    #         isPrime[i] = isPrime[iT] = 0

def _sinusoid_():
    pre()
    for _ in range(int(input())):
        n = int(input())
        for i in range(13, n):
            iT = int(str(i)[::-1])
            if i < iT < n and isPrime[i] == 1 and isPrime[iT] == 1:
                print(i, iT, end = ' ')
        print()

if __name__ == "__main__":
    _sinusoid_()