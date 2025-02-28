import sys

def _sinusoid_():
    a = []
    for i in range(int(sys.stdin.readline())):
        a.append(int(sys.stdin.readline()))
    max1, max2 = float("-inf"), float("-inf")
    for i in a:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2:
            max2 = i
    print(f"Silver = {max2:}")

if __name__ == "__main__":
    _sinusoid_()