class Bill:
    def __init__(self, ID, name, quantity, price, rebate):
        self.ID = ID
        self.name = name
        self.quantity = quantity
        self.price = price
        self.rebate = rebate
        self.total = price * quantity - rebate

    def __lt__(self, other):
        return self.total > other.total

    def __str__(self):
        return f"{self.ID} {self.name} {self.quantity} {self.price} {self.rebate} {self.total}"

def _sinusoid_():
    bills = []
    for _ in range(int(input())):
        ID = input()
        name = input()
        quantity = int(input())
        price = int(input())
        rebate = int(input())
        bills.append(Bill(ID, name, quantity, price, rebate))
    print(*sorted(bills), sep = '\n')

if __name__ == "__main__":
    _sinusoid_()