for i in range(int(input())):
    s1 = input()
    s2 = input()
    print(f"Test {i + 1}:", end = ' ')
    print("YES" if sorted(s1) == sorted(s2) else "NO")          