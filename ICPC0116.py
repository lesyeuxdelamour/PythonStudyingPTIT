def _sinusoid_():
    for _ in range(int(input())):
        n = input()
        print("YES" if n[0] == n[-1] else "NO")

if __name__ == "__main__":
    _sinusoid_()