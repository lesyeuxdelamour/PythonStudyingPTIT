from itertools import permutations

def _sinusoid_():
    for _ in range(int(input())):
        perms = [''.join(map(str, p)) for p in permutations(range(int(input()), 0, -1))]
        print(len(perms))
        print(*perms)

if __name__ == "__main__":
    _sinusoid_()