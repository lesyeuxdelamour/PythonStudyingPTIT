def isCollinear(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)

def _sinusoid_():
    n = int(input())
    points = []
    for _ in range(n):
        points.append(tuple(map(int, input().split())))
    for i in range(2, n):
        if not isCollinear(*points[0], *points[1], *points[i]):
            print("Yes")
            print(1, 2, i + 1)
            return
    print("No")

if __name__ == "__main__":
    _sinusoid_()