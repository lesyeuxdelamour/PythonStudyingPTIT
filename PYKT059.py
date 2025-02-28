from collections import deque

def DFS(adj, u, v):
    visited = set()
    st = deque([u])
    visited.add(u)
    while st:
        tmp = st.pop()
        for i in adj[tmp]:
            if i not in visited:
                st.append(tmp)
                st.append(i)
                visited.add(i)
    return visited

def _sinusoid_():
    v, e, u = map(int, input().split())
    adj = [[] for _ in range(v + 1)]
    for _ in range(e):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)
    visited = DFS(adj, u, v)
    cnt = 0
    for i in range(1, v + 1):
        if i not in visited:
            print(i)

if __name__ == "__main__":
    _sinusoid_()