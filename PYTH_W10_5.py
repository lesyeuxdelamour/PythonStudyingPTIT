while True:
    n = int(input())
    if n == -1:
        break
    print("YES" if n % 11 == 0 else "NO")