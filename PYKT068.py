class Subject:
    def __init__(self, ID, name, test):
        self.ID = ID
        self.name = name
        self.test = test

    def __lt__(self, other):
        return self.ID < other.ID

def _sinusoid_():
    subjects = []
    for _ in range(int(input())):
        ID = input()
        name = input()
        test = input()
        subjects.append(Subject(ID, name, test))
    for subject in sorted(subjects):
        print(subject.ID, subject.name, subject.test)    

if __name__ == "__main__":
    _sinusoid_()