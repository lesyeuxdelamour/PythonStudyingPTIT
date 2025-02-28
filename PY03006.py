import re
from collections import Counter

def _sinusoid_():
    inp = ""
    for _ in range(int(input())):
        inp += input().lower() + ' '
    inp = re.findall(r'[a-z]+', inp)
    freq = sorted(Counter(inp).items(), key = lambda x: (-x[1], x[0]))
    for word, count in freq:
        print(word, count)

if __name__ == "__main__":
    _sinusoid_()