a = []

while len(a) < 10:
    a += list(map(int, input().split()))

a = [i % 42 for i in a]

print(len(set(a)))