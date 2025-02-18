def _sinusoid_():
    for _ in range(int(input())):
        s = input()
        res, tmp = float("inf"), ""
        for i in s:
            if i.isdigit():
                tmp += i
            else:
                if tmp:
                    res = min(res, int(tmp))
                tmp = ""
        if tmp:
            res = min(res, int(tmp))
        print(res)

if __name__ == "__main__":
    _sinusoid_()