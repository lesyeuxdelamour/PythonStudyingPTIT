class Matrix:
    def __init__(self, row, col, data):
        self.row = row
        self.col = col
        self.data = data

    def transpose(self):
        transData = [[self.data[j][i] for j in range(self.row)] for i in range(self.col)]
        return Matrix(self.col, self.row, transData)

    def __mul__(self, other):
        res = [[0] * other.col for _ in range(self.row)]
        for i in range(self.row):
            for j in range(other.col):
                for k in range(self.col):
                    res[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(self.row, other.col, res)

    def __str__(self):
        return '\n'.join(' '.join(map(str, x)) for x in self.data)

def _sinusoid_():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        a = [list(map(int, input().split())) for _ in range(n)]
        matrix = Matrix(n, m, a)
        print(matrix * matrix.transpose())

if __name__ == "__main__":
    _sinusoid_()