def change(s1, s2, p, q):
    m, n = str(min(p, q)), str(max(p, q))
    min1 = int(s1.replace(n, m))
    min2 = int(s2.replace(n, m))
    max1 = int(s1.replace(m, n))
    max2 = int(s2.replace(m, n))
    return min1 + min2, max1 + max2
    
def _sinusoid_():
    for _ in range(int(input())):
        p, q = map(int, input().split())
        inp = input().split()
        if len(inp) > 1:
            s1, s2 = inp[0], inp[1]
        else:
            s1, s2 = inp[0], input()
        print(*change(s1, s2, p, q))

if __name__ == "__main__":
    _sinusoid_()