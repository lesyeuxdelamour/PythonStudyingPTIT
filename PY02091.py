from collections import deque

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def BFS(xS, yS, xE, yE, points):
    q = deque([(xS, yS, 0)])
    points.remove((xS, yS))
    while q:
        x, y, step = q.popleft()
        if x == xE and y == yE:
            return step
        for k in range(8):
            xK = x + dx[k]
            yK = y + dy[k]
            if (xK, yK) in points:
                points.remove((xK, yK))
                q.append((xK, yK, step + 1))
    return -1

def _sinusoid_():
    for _ in range(int(input())):
        xS, yS, xE, yE = map(int, input().split())
        points = set()
        for _ in range(int(input())):
            x, y1, y2 = map(int, input().split())
            for y in range(y1, y2 + 1):
                points.add((x, y))
        print(BFS(xS, yS, xE, yE, points))

if __name__ == "__main__":
    _sinusoid_()