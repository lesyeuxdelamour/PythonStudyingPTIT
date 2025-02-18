from collections import deque

def solve(a):
    st = deque()
    for i in a:
        if st and (i + st[-1]) & 1 == 0:
            st.pop()
        else:
            st.append(i)
    return len(st)

def _sinusoid_():
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a))

if __name__ == "__main__":
    _sinusoid_()