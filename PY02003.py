from bisect import bisect_left
from heapq import heappush, heappop

a = []
seen = set()
heap = [1]

seen.add(1)

while heap:
    x = heappop(heap)
    if x > 1e18:
        break
    a.append(x)
    for i in [2, 3, 5]:
        tmp = x * i
        if tmp not in seen:
            seen.add(tmp)
            heappush(heap, tmp)

for _ in range(int(input())):
    n = int(input())
    idx = bisect_left(a, n)
    print(idx + 1 if a[idx] == n else "Not in sequence")