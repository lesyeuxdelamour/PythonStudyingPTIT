def _sinusoid_():
    s = input()
    mp = dict()
    for i in range(0, len(s) - 1, 2):
        mp[s[i:i + 2]] = mp.get(s[i:i + 2], 0) + 1
    for i in mp:
        print(i, mp[i])

if __name__ == "__main__":
    _sinusoid_()