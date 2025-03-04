class Student:
    def __init__(self, ID, name, classID):
        self.ID = ID
        self.name = name
        self.classID = classID
        self.grade = 10

    def update(self, s):
        late = s.count('m')
        absent = s.count('v')
        grade = max(0, 10 - absent * 2 - late)
        self.grade = f"{grade}" if grade > 0 else "0 KDDK"

    def __str__(self):
        return f"{self.ID} {self.name} {self.classID} {self.grade}"

def _sinusoid_():
    students = {}
    n = int(input())
    for _ in range(n):
        ID = input()
        name = input()
        classID = input()
        students[ID] = Student(ID, name, classID)
    for _ in range(n):
        ID, check = input().split()
        students[ID].update(check)
    print(*students.values(), sep = '\n')

if __name__ == "__main__":
    _sinusoid_()