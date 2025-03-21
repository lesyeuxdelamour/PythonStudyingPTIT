from datetime import datetime

class Session:
    def __init__(self, order, day, hour, roomID):
        self.ID = f"C{order:03}"
        self.date = day + ' ' + hour
        self.roomID = roomID

    def __lt__(self, other):
        return (datetime.strptime(self.date, "%d/%m/%Y %H:%M"), self.ID) < (datetime.strptime(other.date, "%d/%m/%Y %H:%M"), other.ID)

    def __str__(self):
        return f"{self.ID} {self.date} {self.roomID}"

def _sinusoid_():
    with open("CATHI.in", "r") as file:
        sessions = []
        for i in range(int(file.readline())):
            day = file.readline().strip()
            hour = file.readline().strip()
            roomID = file.readline().strip()
            sessions.append(Session(i + 1, day, hour, roomID))
        print(*sorted(sessions), sep = '\n')

if __name__ == "__main__":
    _sinusoid_()