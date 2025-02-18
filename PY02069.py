def isPalindrome(n):
    if len(n) < 2:
        return False
    return n == n[::-1]

def findMaxPalindrome(a):
    a.sort(reverse = True)
    for i in a:
        if isPalindrome(i):
            return i
    return "-1"

def _sinusoid_():
    n, m = map(int, input().split())
    a, tmp = [], []
    for _ in range(n):
        inp = list(input().split())
        a.append(inp)
        tmp += inp
    x = findMaxPalindrome(tmp)
    if x == "-1":
        print("NOT FOUND")
    else:
        print(x)
        for i in range(n):
            for j in range(m):
                if a[i][j] == x:
                    print(f"Vi tri [{i}][{j}]")   

if __name__ == "__main__":
    _sinusoid_()