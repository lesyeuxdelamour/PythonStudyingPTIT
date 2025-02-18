def _sinusoid_():
    s = input()
    k = int(input())
    mp = dict()
    for i in range(0, len(s) - 1, 2):
        mp[s[i:i + 2]] = mp.get(s[i:i + 2], 0) + 1
    res = sorted(i for i in mp if mp[i] >= k)
    if res:
        for i in res:
            print(i, mp[i])
    else:
        print("NOT FOUND")

if __name__ == "__main__":
    _sinusoid_()