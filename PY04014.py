from decimal import Decimal, ROUND_HALF_UP

class Student:
    def __init__(self, order, name, scores):
        self.ID = f"HS{order:02}"
        self.name = name
        self.score = self.calc(scores)

    @staticmethod
    def calc(scores):
        score = (scores[0] * 2 + scores[1] * 2 + sum(scores[2:])) / 12
        return Decimal(score).quantize(Decimal("0.1"), ROUND_HALF_UP)

    def classify(self):
        if self.score >= Decimal("9.0"):
            return "XUAT SAC"
        if self.score >= Decimal("8.0"):
            return "GIOI"
        if self.score >= Decimal("7.0"):
            return "KHA"
        if self.score >= Decimal("5.0"):
            return "TB"
        return "YEU"

    def __lt__(self, other):
        return (self.score, other.ID) > (other.score, self.ID)

    def __str__(self):
        return f"{self.ID} {self.name} {self.score} {self.classify()}"

def _sinusoid_():
    students = []
    for i in range(int(input())):
        name = input()
        scores = list(map(Decimal, input().split()))
        students.append(Student(i + 1, name, scores))
    print(*sorted(students), sep = '\n')

if __name__ == "__main__":
    _sinusoid_()