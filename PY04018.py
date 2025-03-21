class Teacher:
    def __init__(self, order, name, xtID, scoreIT, score):
        self.ID = f"GV{order:02}"
        self.name = name
        subjects = {
            'A': "TOAN",
            'B': "LY",
            'C': "HOA"
        }
        self.subject = subjects[xtID[0]]
        self.total = self.calc(scoreIT, score, xtID[1])

    @staticmethod
    def calc(scoreIT, score, priority):
        total = scoreIT * 2 + score
        if priority == '1':
            return total + 2.0
        if priority == '2':
            return total + 1.5 
        if priority == '3':
            return total + 1.0
        return total

    def result(self):
        return "TRUNG TUYEN" if self.total >= 18 else "LOAI"

    def __lt__(self, other):
        return self.total > other.total

    def __str__(self):
        return f"{self.ID} {self.name} {self.subject} {self.total:.1f} {self.result()}"

def _sinusoid_():
    teachers = []
    for i in range(int(input())):
        name = input()
        xtID = input()
        scoreIT = float(input())
        score = float(input())
        teachers.append(Teacher(i + 1, name, xtID, scoreIT, score))
    print(*sorted(teachers), sep = '\n')

if __name__ == "__main__":
    _sinusoid_()