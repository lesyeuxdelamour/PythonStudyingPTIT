from decimal import Decimal, ROUND_HALF_UP

class Student:
    def __init__(self, order, name, scores):
        self.ID = f"HS{str(order).zfill(2)}"
        self.name = name
        self.score = self.calc(scores)
        self.classification = self.classify(self.score)

    @staticmethod
    def calc(scores):
        score = (scores[0] * 2 + scores[1] * 2 + sum(scores[2:])) / 12
        return Decimal(score).quantize(Decimal("0.1"), rounding = ROUND_HALF_UP)

    @staticmethod
    def classify(scores):
        if scores >= Decimal("9.0"):
            return "XUAT SAC"
        if scores >= Decimal("8.0"):
            return "GIOI"
        if scores >= Decimal("7.0"):
            return "KHA"
        if scores >= Decimal("5.0"):
            return "TB"
        return "YEU"

    def __lt__(self, other):
        return (self.score, other.ID) > (other.score, self.ID)

    def __str__(self):
        return f"{self.ID} {self.name} {self.score} {self.classification}"

def _sinusoid_():
    students = []
    for i in range(int(input())):
        name = input()
        scores = list(map(Decimal, input().split()))
        students.append(Student(i + 1, name, scores))
    for student in sorted(students):
        print(student)

if __name__ == "__main__":
    _sinusoid_()