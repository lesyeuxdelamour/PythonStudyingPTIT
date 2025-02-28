import sys

def _sinusoid_():
    a = []
    for i in range(int(sys.stdin.readline()) - 1):
        a.append(int(sys.stdin.readline()))
    ans = 1
    for i in sorted(a):
        if i != ans:
            print(ans)
            break
        else: 
            ans += 1

if __name__ == "__main__":
    _sinusoid_()