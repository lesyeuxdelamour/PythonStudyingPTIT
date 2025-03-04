class Candidate:
    def __init__(self, order, name, score, ethnic, area):
        self.ID = f"TS{order:02}"
        self.name = self.standard(name)
        self.score = self.calc(score, ethnic, area)
    
    @staticmethod
    def standard(s):
        return ' '.join(s.split()).title()
    
    @staticmethod
    def calc(score, ethnic, area):
        if ethnic != "Kinh":
            score += 1.5
        if area == 1:
            score += 1.5
        elif area == 2:
            score += 1
        return score

    def result(self):
        return "Do" if self.score >= 20.5 else "Truot"

    def __lt__(self, other):
        return (self.score, other.ID) > (other.score, self.ID)

    def __str__(self):
        return f"{self.ID} {self.name} {self.score:.1f} {self.result()}"

def _sinusoid_():
    candidates = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        ethnic = input()
        area = int(input())
        candidates.append(Candidate(i + 1, name, score, ethnic, area))
    print(*sorted(candidates), sep = '\n')

if __name__ == "__main__":
    _sinusoid_()