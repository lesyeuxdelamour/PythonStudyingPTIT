def _sinusoid_():
    n = input()
    while len(n) > 1:
        l = len(n)
        n = str(int(n[l // 2:]) + int(n[:l // 2]))
        print(n)

if __name__ == "__main__":
    _sinusoid_()