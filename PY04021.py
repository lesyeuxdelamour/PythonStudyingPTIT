class Gamer:
    def __init__(self, ID, name, start, end):
        self.ID = ID
        self.name = name
        h1, m1 = map(int, start.split(':'))
        h2, m2 = map(int, end.split(':'))
        self.time = (h2 * 60 + m2) - (h1 * 60 + m1)
        self.hour = self.time // 60
        self.min = self.time % 60

    def __lt__(self, other):
        return self.time > other.time

    def __str__(self):
        return f"{self.ID} {self.name} {self.hour} gio {self.min} phut"

def _sinusoid_():
    gamers = []
    for _ in range(int(input())):
        ID = input()
        name = input()
        start = input()
        end = input()
        gamers.append(Gamer(ID, name, start, end))
    print(*sorted(gamers), sep = '\n')

if __name__ == "__main__":
    _sinusoid_()