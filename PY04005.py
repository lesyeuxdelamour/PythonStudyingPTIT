from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def length(a, b):
        return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y))

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        AB = Point.length(self.a, self.b) 
        BC = Point.length(self.b, self.c)
        CA = Point.length(self.c, self.a)
        if AB + BC <= CA or BC + CA <= AB or CA + AB <= BC:
            return "INVALID"
        return f"{AB + BC + CA:.3f}" 

def _sinusoid_():
    inp, tc = [], int(input())
    for _ in range(tc):
        inp += list(map(float, input().split()))
    for i in range(0, 6 * tc, 6):
        x1, y1, x2, y2, x3, y3 = inp[i:i + 6]
        print(Triangle(Point(x1, y1), Point(x2, y2), Point(x3, y3)).perimeter())

if __name__ == "__main__":
    _sinusoid_()    