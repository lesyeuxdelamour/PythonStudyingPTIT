def sumDigit(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum
    
def _sinusoid_():
    while True:
        inp = input()
        if inp == "-1":
            break
        y, z = map(int, inp.split())
        x = z // sumDigit(y)
        print(x)

if __name__ == "__main__":
    _sinusoid_()