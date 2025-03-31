digits = "0123456789ABCDEF"

def convert(n, b):
    res = ""
    while n > 0:
        res += digits[n % b]
        n //= b
    return res[::-1]

def _sinusoid_():
    for _ in range(int(input())):
        b, n = int(input()), int(input(), 2)
        print(convert(n, b))

if __name__ == "__main__":
    _sinusoid_()