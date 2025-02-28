from collections import deque

def BFS(adj, u, v, e, n):
    visited = set()
    visited.add(e)
    q = deque([u])
    visited.add(u)
    while q:
        tmp = q.popleft()
        if tmp == v:
            return False
        for i in adj[tmp]:
            if i not in visited:
                q.append(i)
                visited.add(i)
    return True

def _sinusoid_():
    for _ in range(int(input())):
        n, m, u, v = map(int, input().split())
        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            x, y = map(int, input().split())
            adj[x].append(y)  
        cnt = 0
        for i in range(1, n + 1):
            if i != u and i != v and BFS(adj, u, v, i, n):
                cnt += 1
        print(cnt)

if __name__ == "__main__":
    _sinusoid_()    