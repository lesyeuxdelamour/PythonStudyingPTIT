from collections import Counter

for _ in range(int(input())):
    n = int(input())
    sortedFreq = sorted(Counter(int(input()) for _ in range(n)).items(), key = lambda x: (-x[1], x[0]))
    print(sortedFreq[0][0])