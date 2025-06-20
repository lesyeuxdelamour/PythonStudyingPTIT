class Student:
    def __init__(self, name, correct, submit):
        self.name = name
        self.correct = correct
        self.submit = submit

    def __lt__(self, other):
        return (other.correct, self.submit, self.name) < (self.correct, other.submit, other.name)

    def __str__(self):
        return f"{self.name} {self.correct} {self.submit}"

def _sinusoid_():
    students = []
    for _ in range(int(input())):
        name = input()
        correct, submit = map(int, input().split())
        students.append(Student(name, correct, submit))
    print(*sorted(students), sep = '\n')

if __name__ == "__main__":
    _sinusoid_()