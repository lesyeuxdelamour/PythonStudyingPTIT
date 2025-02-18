from collections import Counter

def _sinusoid_():
    n, m = map(int, input().split())
    sortedFreq = sorted(Counter(list(map(int, input().split()))).items(), key = lambda x : (-x[1], x[0]))
    if len(sortedFreq) < 2 or sortedFreq[0][1] == sortedFreq[1][1]:
        print("NONE")
    else:
        print(sortedFreq[1][0])

if __name__ == "__main__":
    _sinusoid_()