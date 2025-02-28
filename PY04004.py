from math import gcd

class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den
        self.simplify()

    def simplify(self):
        tmp = gcd(self.num, self.den)
        self.num //= tmp
        self.den //= tmp
        if self.den < 0:
            self.num = -self.num
            self.den = -self.den
        return self

    def __add__(self, other):
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __str__(self):
        return f"{self.num}/{self.den}"

def _sinusoid_():
    inp = input().split()
    frac1, frac2 = Fraction(int(inp[0]), int(inp[1])), Fraction(int(inp[2]), int(inp[3]))
    print(frac1 + frac2)

if __name__ == "__main__":
    _sinusoid_()