from itertools import combinations

n, k = map(int, input().split())

names = sorted(set(input().split()))

for team in combinations(names, k):
    print(' '.join(team))