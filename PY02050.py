from collections import deque

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    st = deque()
    for i in range(n):
        while st and a[st[-1]] <= a[i]:
            st.pop()
        if st:
            print(i - st[-1], end = ' ')
        else:
            print(i + 1, end = ' ')
        st.append(i)
    print()
