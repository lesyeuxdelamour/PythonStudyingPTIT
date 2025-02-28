import re
from collections import deque

def check(x, y, z, op):
    if op == '+':
        return x + y == z
    if op == '-':
        return x - y == z
    if op == '*':
        return x * y == z
    if op == '/':
        if x % y == 0:
            return x // y == z
    return False

def gen(s):
    if len(s) == 1:
        if s == '?':
            return [i for i in "+-*/"]
        return [s]
    if s[0] == '?':
        left = [str(i) for i in range(1, 10)]
    else:
        left = [s[0]]
    if s[1] == '?':
        right = [str(i) for i in range(0, 10)]
    else:
        right = [s[1]]
    return [i + j for i in left for j in right]

def solve(x, y, z, op):
    x, y, z, op = gen(x), gen(y), gen(z), gen(op)
    for i in x:
        for j in y:
            for k in z:
                for l in op:
                    if check(int(i), int(j), int(k), l):
                        print(f"{i} {l} {j} = {k}")
                        return
    print("WRONG PROBLEM!")

def _sinusoid_():
    for _ in range(int(input())):
        x, op, y, eq, z = input().split()
        solve(x, y, z, op)

if __name__ == "__main__":
    _sinusoid_()