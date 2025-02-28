def maxWhite(n, k):
    size = 6 * n * n
    if k >= size:
        return size
    corners, edges, faces = 8, 12 * (n - 2), 6 * (n - 2) ** 2
    total = min(k, corners) * 3
    k -= min(k, corners)
    total += min(k, edges) * 2
    k -= min(k, edges)
    total += min(k, faces)
    k -= faces
    return total

def _sinusoid_():
    n, k = map(int, input().split())
    print(maxWhite(n, k))

if __name__ == "__main__":
    _sinusoid_()

#Todo: fix WA
#Input: 5 3
#Output: 14