triplet = [0] * 1000008

def pre():
    isPrime = [1] * 1000001
    isPrime[0] = isPrime[1] = 0
    for i in range(2, 1001):
        if isPrime[i] == 1:
            for j in range(i * i, 1000001, i):
                isPrime[j] = 0
    for i in range(5, 1000001):
        if isPrime[i] == 1 and isPrime[i + 6]:
            if isPrime[i + 2]:
                triplet[i + 7] += 1
            if isPrime[i + 4]:
                triplet[i + 7] += 1
        triplet[i] += triplet[i - 1]

def _sinusoid_():
    pre()
    for _ in range(int(input())):
        print(triplet[int(input())])

if __name__ == "__main__":
    _sinusoid_()