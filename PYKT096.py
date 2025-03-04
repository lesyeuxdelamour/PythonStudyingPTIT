class Candidate:
    def __init__(self, order, name, teamID, team):
        self.ID = f"C{order:03}"
        self.name = name
        self.teamID = teamID
        self.team = team

    def __lt__(self, other):
        return self.name < other.name

    def __str__(self):
        return f"{self.ID} {self.name} {self.teamID} {self.team}"

def _sinusoid_():
    teams, candidates = {}, []
    for i in range(int(input())):
        ID = input()
        name = input()
        teams[f"Team{i + 1:02}"] = ID, name
    for i in range(int(input())):
        name = input()
        teamID = input()
        candidates.append(Candidate(i + 1, name, teams[teamID][0], teams[teamID][1]))
    print(*sorted(candidates), sep = '\n')

if __name__ == "__main__":
    _sinusoid_()