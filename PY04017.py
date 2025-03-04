class Rider:
    def __init__(self, name, team, time):
        self.ID = self.acronym(name, team)
        self.name = name
        self.team = team
        h, m = map(int, time.split(':'))
        self.speed = 120 / (h - 6 + m / 60)

    @staticmethod
    def acronym(name, team):
        return ''.join(s[0] for s in (team + ' ' + name).split())

    def __lt__(self, other):
        return self.speed > other.speed

    def __str__(self):
        return f"{self.ID} {self.name} {self.team} {round(self.speed)} Km/h"

def _sinusoid_():
    riders = []
    for _ in range(int(input())):
        name = input()
        team = input()
        time = input()
        riders.append(Rider(name, team, time))
    print(*sorted(riders), sep = '\n')

if __name__ == "__main__":
    _sinusoid_()