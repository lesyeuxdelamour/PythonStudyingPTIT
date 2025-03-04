class Employee:
    def __init__(self, ID, name, depart, wage, days):
        self.ID = ID
        self.name = name
        self.depart = depart
        self.income = self.calc(ID, wage, days)

    @staticmethod
    def calc(ID, wage, days):
        group = ID[0]
        years = int(ID[1:3])
        table = {
            'A': [(1, 3, 10), (4, 8, 12), (9, 15, 14), (16, 100, 20)],
            'B': [(1, 3, 10), (4, 8, 11), (9, 15, 13), (16, 100, 16)],
            'C': [(1, 3, 9), (4, 8, 10), (9, 15, 12), (16, 100, 14)],
            'D': [(1, 3, 8), (4, 8, 9), (9, 15, 11), (16, 100, 13)]
        }
        for start, end, coefficient in table[group]:
            if start <= years <= end:
                return coefficient * wage * days * 1000
        return 0

    def __str__(self):
        return f"{self.ID} {self.name} {self.depart} {self.income}"

def _sinusoid_():
    departs, employees = {}, []
    for _ in range(int(input())):
        inp = input().split()
        ID, name = inp[0], ' '.join(inp[1:])
        departs[ID] = name
    for _ in range(int(input())):
        ID = input()
        name = input()
        wage = int(input())
        days = int(input())
        employees.append(Employee(ID, name, departs[ID[3:5]], wage, days))
    print(*employees, sep = '\n')

if __name__ == "__main__":
    _sinusoid_()