def height(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def _sinusoid_():
    while True:
        inp = input()
        if inp == "-1":
            break
        n, h = map(int, inp.split())
        cnt = 0
        for i in range(n):
            if height(i) == h:
                cnt += 1
        print(cnt)

if __name__ == "__main__":
    _sinusoid_()