def _sinusoid_():
    m = int(input())
    v = int(input())
    t = int(input())
    d = input()
    s = v * t
    if d == 'A':
        x = -s % m
    elif d == 'C':
        x = s % m
    print(x)

if __name__ == "__main__":
    _sinusoid_()