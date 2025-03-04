class Employee:
    def __init__(self, order, name, theory, practice):
        self.ID = f"TS0{order}"
        self.name = name
        self.score = ((theory if theory <= 10 else theory / 10) + (practice if practice <= 10 else practice / 10)) / 2

    def result(self.score):
        if self.score > 9.5:
            return "XUAT SAC"
        if self.score >= 8:
            return "DAT"
        if self.score >= 5:
            return "CAN NHAC"
        return "TRUOT"

    def __lt__(self, other):
        return self.score > other.score

    def __str__(self):
        return f"{self.ID} {self.name} {self.score:.2f} {self.result()}"

def _sinusoid_():
    employees = []
    for i in range(int(input())):
        name = input()
        theory = float(input())
        practice = float(input())
        employees.append(Employee(i + 1, name, theory, practice))
    print(*sorted(employees), sep = '\n')

if __name__ == "__main__":
    _sinusoid_()