class Rectangle:
    def __init__(self, length, width, colour):
        self.length = length
        self.width = width
        self.colour = colour

    def perimeter(self):
        return (self.length + self.width) * 2

    def area(self):
        return self.length * self.width

    def color(self):
        return self.colour.capitalize()

def _sinusoid_():
    inp = input().split()
    if int(inp[0]) <= 0 or int(inp[1]) <= 0:
        print("INVALID")
        return
    rec = Rectangle(int(inp[0]), int(inp[1]), inp[2])
    print(f"{rec.perimeter()} {rec.area()} {rec.color()}")

_sinusoid_()

# Hàm main đề lỗi
# if __name__ == "__main__":
#     _sinusoid_()