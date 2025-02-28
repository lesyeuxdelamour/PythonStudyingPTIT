def check(mp, n):
    for i in mp:
        if mp[i] != n - 1 and mp[i] != 1:
            return "No"
    return "Yes"

def _sinusoid_():
    n = int(input())
    mp = dict()
    for _ in range(n - 1):
        x, y = map(int, input().split())
        mp[x] = mp.get(x, 0) + 1
        mp[y] = mp.get(y, 0) + 1
    print(check(mp, n))

if __name__ == "__main__":
    _sinusoid_()