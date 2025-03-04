class Station:
    def __init__(self, order, name):
        self.ID = f"T{order:02}"
        self.name = name
        self.rainfall = 0
        self.time = 0

    def update(self, start, end, rain):
        h1, m1 = map(int, start.split(':'))
        h2, m2 = map(int, end.split(':'))
        self.time += (h2 * 60 + m2) - (h1 * 60 + m1)
        self.rainfall += rain

    def avg(self):
        return self.rainfall / (self.time / 60)

    def __str__(self):
        return f"{self.ID} {self.name} {self.avg():.2f}"

def _sinusoid_():
    stations, order = {}, 1
    for _ in range(int(input())):
        name = input()
        start = input()
        end = input()
        rain = float(input())
        if name not in stations:
            stations[name] = Station(order, name)
            order += 1
        stations[name].update(start, end, rain)
    print(*stations.values(), sep = '\n')

if __name__ == "__main__":
    _sinusoid_()
