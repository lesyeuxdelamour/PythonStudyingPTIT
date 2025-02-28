def _sinusoid_():
    with open("CONTACT.in", "r") as file:
        se = set()
        for line in file:
            se.add(line.lower().strip())
    print(*sorted(se), sep = '\n')

if __name__ == "__main__":
    _sinusoid_()