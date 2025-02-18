def _sinusoid_():
    s = input()
    se = set()
    for i in range(0, len(s) - 1, 2):
        if s[i:i + 2] not in se:
            se.add(s[i:i + 2])
            print(s[i:i + 2], end = ' ')

if __name__ == "__main__":
    _sinusoid_()