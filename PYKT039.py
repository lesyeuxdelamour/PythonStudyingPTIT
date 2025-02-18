def check(a, b):
    a.sort()
    b.sort()
    for i in range(len(a)):
        if a[i] > b[i]:
            return "NO"
    return "YES"

def _sinusoid_():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(check(a, b))

if __name__ == "__main__":
    _sinusoid_()