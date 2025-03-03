class Candidate:
    def __init__(self, name, DOB, score):
        self.name = name
        self.DOB = DOB
        self.score = score

    def __str__(self):
        return f"{self.name} {self.DOB} {self.score:.1f}"

def _sinusoid_():
    name = input()
    DOB = input()
    a, b, c = input(), input(), input()
    score = sum(map(float, [a, b, c]))
    print(Candidate(name, DOB, score))

if __name__ == "__main__":
    _sinusoid_()