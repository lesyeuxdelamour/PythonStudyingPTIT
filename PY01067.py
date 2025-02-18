from collections import deque

def dominantTwo(n = 1000):
    se = set()
    q = deque([("", 0)])
    while q:
        s, cnt = q.popleft()
        if cnt > len(s) / 2:
            se.add(int(s))
            if len(se) > n:
                break
        q.append([s + "0", cnt])
        q.append([s + "1", cnt])
        q.append([s + "2", cnt + 1])
    return sorted(se)

res = dominantTwo()

for _ in range(int(input())):
    print(" ".join(map(str, res[:int(input())])))