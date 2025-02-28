def _sinusoid_():
    with open("DATA.in", "r") as file:
        notInt = []
        for line in file:
            tokens = line.split()
            for token in tokens:
                try:
                    num = int(token)
                    if -2 ** 31 <= num <= 2 ** 31 - 1:
                        continue
                except ValueError:
                    pass
                notInt.append(token)
        print(*sorted(notInt))

if __name__ == "__main__":
    _sinusoid_()