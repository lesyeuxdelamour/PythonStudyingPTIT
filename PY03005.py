import re
from collections import Counter

def _sinusoid_():
    n, k = map(int, input().split())
    inp = ""
    for _ in range(n):
        inp += input().lower() + ' '
    inp = re.findall(r'\b\w+\b', inp) 
    freq = sorted(Counter(inp).items(), key = lambda x: (-x[1], x[0]))
    for word, count in freq:
        if count >= k:
            print(word, count)

if __name__ == "__main__":
    _sinusoid_()