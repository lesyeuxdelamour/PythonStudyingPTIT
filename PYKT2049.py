par = [i for i in range(100001)]
sz = [1] * 100001

def root(u):
    if u == par[u]:
        return u
    par[u] = root(par[u])
    return par[u]

def union(u, v):
    u = root(u)
    v = root(v)
    if u == v:
        return
    if sz[u] < sz[v]:
        u, v = v, u
    sz[u] += sz[v]
    par[v] = u

def _sinusoid_():
    for _ in range(int(input())):
        x, y, z = map(int, input().split())
        if z == 1:
            union(x, y)
        else: # 2
            print(1 if root(x) == root(y) else 0)

if __name__ == "__main__":
    _sinusoid_()