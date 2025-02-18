fac = [1] * 10

def pre():
    for i in range(1, 10):
        fac[i] = fac[i - 1] * i

def _sinusoid_():
    pre()
    for _ in range(int(input())):
        n = input()
        print("Yes" if int(n) == sum(fac[int(i)] for i in n) else "No")

if __name__ == "__main__":
    _sinusoid_()