s1 = set(map(str.lower, input().split()))
s2 = set(map(str.lower, input().split()))

print(*sorted(s1 | s2))
print(*sorted(s1 & s2))
