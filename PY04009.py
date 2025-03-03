class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

def _sinusoid_():
    for _ in range(int(input())):
        inp = list(map(int, input().split()))
        complex1, complex2 = Complex(inp[0], inp[1]), Complex(inp[2], inp[3])
        res1 = (complex1 + complex2) * complex1
        res2 = (complex1 + complex2) * (complex1 + complex2)
        print(res1, res2, sep = ', ')

if __name__ == "__main__":
    _sinusoid_()