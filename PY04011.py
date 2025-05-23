from collections import defaultdict, deque

def Kahn(adj, inDegree, v):
    q = deque()
    for i in range(v):
        if inDegree[i] == 0:
            q.append(i)
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for i in adj[u]:
            inDegree[i] -= 1
            if inDegree[i] == 0:
                q.append(i)
    return len(topo) == v # Tồn tại sắp xếp Topo => Đồ thị không có chu trình

def _sinusoid_():
    ID = {}
    cnt = 0
    adj = defaultdict(list)
    inDegree = defaultdict(int)
    for _ in range(int(input())):
        x, op, y = input().split()
        if x not in ID:
            ID[x] = cnt
            cnt += 1
        if y not in ID:
            ID[y] = cnt
            cnt += 1
        u = ID[x]
        v = ID[y]
        if op == "<":
            adj[u].append(v)
            inDegree[v] += 1
        else: # ">"
            adj[v].append(u)
            inDegree[u] += 1
    if Kahn(adj, inDegree, cnt):
        print("possible")
    else:
        print("impossible")

if __name__ == "__main__":
    _sinusoid_()