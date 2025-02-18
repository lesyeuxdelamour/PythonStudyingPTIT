score = [
    (39, 40, 9.0), 
    (37, 38, 8.5), 
    (35, 36, 8.0), 
    (33, 34, 7.5), 
    (30, 32, 7.0), 
    (27, 29, 6.5), 
    (23, 26, 6.0), 
    (20, 22, 5.5), 
    (16, 19, 5.0), 
    (13, 15, 4.5), 
    (10, 12, 4.0), 
    (7, 9, 3.5), 
    (5, 6, 3.0), 
    (3, 4, 2.5)
]

def convert(n):
    for lower, upper, band in score:
        if lower <= int(n) <= upper:
            return band
    return 1.0

def calc(reading, listening, speaking, writing):
    reading = convert(reading)
    listening = convert(listening)
    overall = (reading + listening + speaking + writing) / 4
    if overall - int(overall) < 0.25:
        overall = float(int(overall))
    elif 0.25 <= overall - int(overall) < 0.75:
        overall = float(int(overall)) + 0.5
    elif overall - int(overall) >= 0.75:
        overall = float(int(overall)) + 1.0
    return overall

for _ in range(int(input())):
    reading, listening, speaking, writing = map(float, input().split())
    print(calc(reading, listening, speaking, writing))