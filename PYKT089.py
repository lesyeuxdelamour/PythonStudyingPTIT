def _sinusoid_():
    n = int(input())
    a = []
    while len(a) < n:
        a += map(int, input().split())
    even = sorted((i for i in a if i & 1 == 0))
    odd = sorted((i for i in a if i & 1 == 1), reverse = True)
    x, y = 0, 0
    for i in a:
        if i & 1 == 0:
            print(even[x], end = ' ')
            x += 1
        else:
            print(odd[y], end = ' ')
            y += 1

if __name__ == "__main__":
    _sinusoid_()