def convert(n, b):
    res = ""
    while n > 0:
        res += str(n % b)
        n //= b
    return res == res[::-1]

def isBiPalindrome(n, a, b):
    return "YES" if convert(n, a) and convert(n, b) else "NO"

def _sinusoid_():
    while True:
        inp = input()
        if inp == "-1":
            break
        x, a, b = map(int, inp.split())
        print(isBiPalindrome(x, a, b))

if __name__ == "__main__":
    _sinusoid_()

#Todo: fix WA