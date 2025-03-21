from datetime import datetime

class Customer:
    def __init__(self, order, name, room, start, end, fee):
        self.ID = f"KH{order:02}"
        self.name = name
        self.room = room
        self.days = (datetime.strptime(end, "%d/%m/%Y") - datetime.strptime(start, "%d/%m/%Y")).days + 1
        self.bill = self.calc(room[0], self.days, fee)

    @staticmethod
    def calc(floor, days, fee):
        if floor == '1':
            return days * 25 + fee
        if floor == '2':
            return days * 34 + fee
        if floor == '3':
            return days * 50 + fee
        if floor == '4':
            return days * 80 + fee
        return 0

    def __lt__(self, other):
        return self.bill > other.bill

    def __str__(self):
        return f"{self.ID} {self.name} {self.room} {self.days} {self.bill}"

def _sinusoid_():
    customers = []
    for i in range(int(input())):
        name = input()
        room = input()
        start = input().strip()
        end = input().strip()
        fee = int(input())
        customers.append(Customer(i + 1, name, room, start, end, fee))
    print(*sorted(customers), sep = '\n')

if __name__ == "__main__":
    _sinusoid_()