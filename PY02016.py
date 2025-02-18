from collections import Counter

for _ in range(int(input())):
    n = int(input())
    freq = Counter(input().split())
    print(freq.most_common(1)[0][0] if freq.most_common(1)[0][1] > (n // 2) else "NO")