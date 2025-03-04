from decimal import Decimal, ROUND_HALF_UP

class Student:
    def __init__(self, order, name, score):
        self.ID = f"SV{order:02}"
        self.name = self.standard(name)
        self.score = Decimal(score).quantize(Decimal("0.01"), ROUND_HALF_UP)
        self.rank = -1

    @staticmethod
    def standard(s):
        return ' '.join(s.split()).title()

    def __lt__(self, other):
        return (self.score, other.ID) > (other.score, self.ID)

    def __str__(self):
        return f"{self.ID} {self.name} {self.score:.2f} {self.rank}"

def _sinusoid_():
    students = []
    for i in range(int(input())):
        name = input()
        subject1 = float(input())
        subject2 = float(input())
        subject3 = float(input())
        score = (subject1 * 3 + subject2 * 3 + subject3 * 2) / 8
        students.append(Student(i + 1, name, score))
    students.sort()
    students[0].rank = 1
    for i in range(1, len(students)):
        students[i].rank = students[i - 1].rank if students[i].score == students[i - 1].score else i + 1
    print(*students, sep = '\n')

if __name__ == "__main__":
    _sinusoid_()