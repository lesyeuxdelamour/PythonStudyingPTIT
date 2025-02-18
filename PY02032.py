def _sinusoid_():
    s = input()
    print(*sorted(set([s[i:i + 2] for i in range(0, len(s) - 1, 2)])))

if __name__ == "__main__":
    _sinusoid_()