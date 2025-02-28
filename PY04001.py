from math import sqrt
from decimal import Decimal

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x0 = self.x - other.x
        y0 = self.y - other.y
        return f"{sqrt(x0 * x0 + y0 * y0):.4f}"

def _sinusoid_():
    for _ in range(int(input())):
        inp = input().split()
        x = Point(Decimal(inp[0]), Decimal(inp[1]))
        y = Point(Decimal(inp[2]), Decimal(inp[3]))
        print(x.distance(y))

if __name__ == "__main__":
    _sinusoid_()