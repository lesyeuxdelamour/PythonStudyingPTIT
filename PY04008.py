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
        inp, tc = [], int(input())
        while True:
            try:
                inp += list(map(int, input().split()))
            except EOFError:
                break
        idx = 0
        for _ in range(tc):
            n, m = inp[idx], inp[idx + 1]
            idx += 2
            a = [[None] * m for _ in range(n)]
            while len(inp) - idx < n * m:
                inp.append(0)
            for i in range(n):
                for j in range(m):
                    a[i][j] = inp[idx]
                    idx += 1
            matrix = Matrix(n, m, a)
            print(matrix * matrix.transpose())

    if __name__ == "__main__":
        _sinusoid_()