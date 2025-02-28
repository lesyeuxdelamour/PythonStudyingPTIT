class Student:
    def __init__(self, name, correct, submit):
        self.name = name
        self.correct = correct
        self.submit = submit

    def __lt__(self, other):
        if self.correct != other.correct:
            return self.correct > other.correct
        if self.submit != other.submit:
            return self.submit < other.submit
        return self.name < other.name

def _sinusoid_():
    students = []
    for _ in range(int(input())):
        name = input()
        correct, submit = map(int, input().split())
        students.append(Student(name, correct, submit))
    for student in sorted(students):
        print(student.name, student.correct, student.submit)

if __name__ == "__main__":
    _sinusoid_()