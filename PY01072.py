from itertools import combinations

n, k = map(int, input().split())
a = sorted(set(map(int, input().split())))

for c in combinations(a, k):
    print(' '.join(map(str, c)))
