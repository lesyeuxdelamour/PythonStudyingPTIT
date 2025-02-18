def _sinusoid_():
    for _ in range(int(input())):
        s = input()
        x = input()
        print(len(s.split(x)) - 1)

if __name__ == "__main__":
    _sinusoid_()