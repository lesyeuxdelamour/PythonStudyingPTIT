def encode(s):
    l = len(s)
    cnt = 1
    for i in range(l - 1):
        if(s[i] == s[i + 1]):
            cnt += 1
        else:
            print(cnt, s[i], sep = '', end = '')
            cnt = 1
    print(cnt, s[l - 1], sep = '')

tc = int(input())

for _ in range(tc):         
    s = input()
    encode(s)