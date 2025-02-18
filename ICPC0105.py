def _sinusoid_():
    for _ in range(int(input())):
        s = input()
        res, tmp = 0, ""
        for i in s:
            if i.isdigit():
                tmp += i
            else:
                if tmp:
                    res = max(res, int(tmp))
                tmp = ""
        if tmp:
            res = max(res, int(tmp))
        print(res)

if __name__ == "__main__":
    _sinusoid_()