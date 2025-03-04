class Bill:
    def __init__(self, order, name, type, before, after):
        self.ID = f"KH{order:02}"
        self.name = self.standard(name)
        electric = int(after) - int(before)
        self.under, self.over, self.VAT, self.total = self.calc(type, electric) 

    @staticmethod
    def standard(s):
        return ' '.join(s.split()).title()

    @staticmethod
    def calc(type, electric):
        if type == 'A':
            limit = 100
        elif type == 'B':
            limit = 500
        elif type == 'C':
            limit = 200
        under = min(electric, limit) * 450
        over = max(electric - limit, 0) * 1000
        VAT = over // 20
        total = under + over + VAT
        return under, over, VAT, total

    def __lt__(self, other):
        return self.total > other.total

    def __str__(self):
        return f"{self.ID} {self.name} {self.under} {self.over} {self.VAT} {self.total}"

def _sinusoid_():
    bills = []
    for i in range(int(input())):
        name = input()
        type, before, after = input().split()
        bills.append(Bill(i + 1, name, type, before, after))
    print(*sorted(bills), sep = '\n')

if __name__ == "__main__":
    _sinusoid_()