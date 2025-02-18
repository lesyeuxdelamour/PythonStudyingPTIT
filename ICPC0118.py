zodiacSigns = [
    ("Bach Duong", 21, 3, 19, 4),
    ("Kim Nguu", 20, 4, 20, 5),
    ("Song Tu", 21, 5, 20, 6),
    ("Cu Giai", 21, 6, 22, 7),
    ("Su Tu", 23, 7, 22, 8),
    ("Xu Nu", 23, 8, 22, 9),
    ("Thien Binh", 23, 9, 22, 10),
    ("Thien Yet", 23, 10, 22, 11),
    ("Nhan Ma", 23, 11, 21, 12),
    ("Ma Ket", 22, 12, 19, 1),
    ("Bao Binh", 20, 1, 18, 2),
    ("Song Ngu", 19, 2, 20, 3)
]

def findZodiacSign(d, m):
    for name, startDay, startMonth, endDay, endMonth in zodiacSigns:
        if (m == startMonth and d >= startDay) or (m == endMonth and d <= endDay):
            return name
    return "Invalid"

def _sinusoid_():
    for _ in range(int(input())):
        d, m = map(int, input().split())
        print(findZodiacSign(d, m))

if __name__ == "__main__":
    _sinusoid_()