from datetime import datetime

class Session:
    def __init__(self, order, subjectID, name, date, sessionID):
        self.ID = f"T{order:03}"
        self.subjectID = subjectID
        self.name = name
        self.date = date
        self.sessionID = sessionID

    def __lt__(self, other):
        return (datetime.strptime(self.date, "%d/%m/%Y %H:%M"), self.sessionID) < (datetime.strptime(other.date, "%d/%m/%Y %H:%M"), other.sessionID)

    def __str__(self):
        return f"{self.ID} {self.subjectID} {self.name} {self.date} {self.sessionID}"

def _sinusoid_():
    n, m = map(int, input().split())
    subjects, sessions = {}, []
    for i in range(n):
        ID = input()
        name = input()
        subjects[ID] = name
    for i in range(m):
        subjectID, day, hour, sessionID = input().split()
        sessions.append(Session(i + 1, subjectID, subjects[subjectID], day + ' ' + hour, sessionID))
    print(*sorted(sessions), sep = '\n')

if __name__ == "__main__":
    _sinusoid_()