from datetime import datetime

class Film:
    def __init__(self, order, genre, release, name, eps):
        self.ID = f"P{order:03}"
        self.genre = genre
        self.release = release
        self.name = name
        self.eps = eps

    def __lt__(self, other):
        return (datetime.strptime(self.release, "%d/%m/%Y"), self.name, other.eps) < (datetime.strptime(other.release, "%d/%m/%Y"), other.name, self.eps)

    def __str__(self):
        return f"{self.ID} {self.genre} {self.release} {self.name} {self.eps}"

def _sinusoid_():
    n, m = map(int, input().split())
    genres, films = {}, []
    for i in range(n):
        genres[f"TL{i + 1:03}"] = input()
    for i in range(m):
        genreID = input()
        release = input()
        name = input()
        eps = int(input())
        films.append(Film(i + 1, genres[genreID], release, name, eps))
    print(*sorted(films), sep = '\n')

if __name__ == "__main__":
    _sinusoid_()