p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    inp = input()
    if inp == "0":
        break
    k, s = inp.split()
    res = ""
    for i in s:
        res += p[(p.find(i) + int(k)) % 28]
    print(res[::-1])    