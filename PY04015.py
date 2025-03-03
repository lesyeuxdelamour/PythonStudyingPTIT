class Bill:
    def __init__(self, order, name, before, after):
        self.ID = f"KH{str(order).zfill(2)}"
        self.name = name
        self.water = after - before
        self.fee = self.calc(self.water)

    @staticmethod
    def calc(water):
        if water <= 50:
            fee = water * 100
            fee *= 1.02
        elif water <= 100:
            fee = 50 * 100 + (water - 50) * 150
            fee *= 1.03
        else:
            fee = 50 * 100 + 50 * 150 + (water - 100) * 200
            fee *= 1.05
        return round(fee)

    def __lt__(self, other):
        return self.fee > other.fee

    def __str__(self):
        return f"{self.ID} {self.name} {self.fee}"

def _sinusoid_():
    bills = []
    for i in range(int(input())):
        name = input()
        before = int(input())
        after = int(input())
        bills.append(Bill(i + 1, name, before, after))
    for bill in sorted(bills):
        print(bill)

if __name__ == "__main__":
    _sinusoid_()