from collections import deque

def _sinusoid_():
    for _ in range(int(input())):
        st, cnt = deque(), 1
        for c in (input()):
            if c == '(':
                st.append(cnt)
                print(cnt, end = ' ')
                cnt += 1
            elif c == ')':
                print(st[-1], end = ' ')
                st.pop()
        print()

if __name__ == "__main__":
    _sinusoid_()