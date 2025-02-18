def findMax(n):    
    i = len(n) - 2
    while i >= 0 and n[i] <= n[i + 1]:
        i -= 1
    if i < 0:
        return "-1"
    maxIdx = -1
    for j in range(i + 1, len(n)):
        if n[j] < n[i] and (maxIdx == -1 or n[j] > n[maxIdx]):
            maxIdx = j
    n[i], n[maxIdx] = n[maxIdx], n[i]
    if n[0] == '0':
        return "-1"
    return "".join(n)

def _sinusoid_():
    for _ in range(int(input())):
        n = list(input())
        print(findMax(n))

if __name__ == "__main__":
    _sinusoid_()