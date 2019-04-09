from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, Matrix, other):
        self.matrix1 = Matrix
        self.matrix2 = other


class Matrix:
    def __init__(self, strings=[[]]):
        self.strings = deepcopy(strings)

    def __str__(self):
        columns = len(self.strings[0])
        rows = len(self.strings)
        string = ''
        for i in range(rows):
            for j in range(columns - 1):
                string += (str(self.strings[i][j]) + '\t')
            string += (str(self.strings[i][columns - 1]) + '\n')
        return string[:-1]

    def size(self):
        return len(self.strings), len(self.strings[0])

    def __add__(self, other):
        rows = len(self.strings)
        columns = len(self.strings[0])
        if rows == len(other.strings) and columns == len(other.strings[0]):
            result = deepcopy(self.strings)
            for i in range(rows):
                for j in range(columns):
                    result[i][j] = self.strings[i][j] + other.strings[i][j]
        else:
            raise MatrixError(self, other)
        return Matrix(result)

    def __mul__(self, other):
        rowsself = len(self.strings)
        columnsself = len(self.strings[0])
        if isinstance(other, int) or isinstance(other, float):
            result = deepcopy(self.strings)
            for i in range(rowsself):
                for j in range(columnsself):
                    result[i][j] = self.strings[i][j] * other
        elif isinstance(other, Matrix):
            rowsother = len(other.strings)
            columnsother = len(other.strings[0])
            if columnsself == rowsother:
                result = [[0]]
                rowsres = rowsself
                columnsres = columnsother
                for i in range(rowsres - 1):
                    for j in range(columnsres - 1):
                        for k in range(columnsself):
                            result[i][j] += (
                                self.strings[i][k] * other.strings[k][j]
                            )
                        result[i].append(0)
                    for k in range(columnsself):
                        result[i][columnsres - 1] += (
                            self.strings[i][k] * other.strings[k][
                                columnsres - 1
                            ]
                        )
                    result.append([0])
                for j in range(columnsres - 1):
                    for k in range(columnsself):
                        result[rowsres - 1][j] += (
                            self.strings[rowsres - 1][k] * other.strings[k][j]
                        )
                    result[rowsres - 1].append(0)
                for k in range(columnsself):
                    result[rowsres - 1][columnsres - 1] += (
                        self.strings[rowsres - 1][k] * other.strings[k][
                            columnsres - 1
                        ]
                    )
            else:
                raise MatrixError(self, other)
        return Matrix(result)

    __rmul__ = __mul__

    def transpose(self):
        rows = len(self.strings)
        columns = len(self.strings[0])
        result = [[0]]
        for i in range(columns - 1):
            for j in range(rows - 1):
                result[i][j] = self.strings[j][i]
                result[i].append(0)
            result[i][rows - 1] = self.strings[rows - 1][i]
            result.append([0])
        for j in range(rows - 1):
            result[columns - 1][j] = self.strings[j][columns - 1]
            result[columns - 1].append(0)
        result[columns - 1][rows - 1] = self.strings[rows - 1][columns - 1]
        self.strings = result
        return Matrix(result)

    def transposed(object):
        rows = len(object.strings)
        columns = len(object.strings[0])
        result = [[0]]
        for i in range(columns - 1):
            for j in range(rows - 1):
                result[i][j] = object.strings[j][i]
                result[i].append(0)
            result[i][rows - 1] = object.strings[rows - 1][i]
            result.append([0])
        for j in range(rows - 1):
            result[columns - 1][j] = object.strings[j][columns - 1]
            result[columns - 1].append(0)
        result[columns - 1][rows - 1] = object.strings[rows - 1][columns - 1]
        return Matrix(result)

    transposed = staticmethod(transposed)

    def solve(self, other):
        m, n = self.size()
        col = 0
        for curstr in range(m):
            col = curstr
            while col < n:
                i = curstr
                while self.strings[i][col] == 0:
                    i += 1
                if i == m:
                    col += 1
                elif m > i > curstr:
                    self[i], self[curstr] = self[curstr], self[i]
                    other[i], other[curstr] = other[curstr], other[i]
                else:
                    for p in range(m):
                        if p != curstr:
                            koef = self.strings[p][col] / self.strings[
                                curstr
                            ][col]
                            for q in range(n):
                                self.strings[p][q] -= (
                                    koef * self.strings[curstr][q]
                                )
                            other[p] -= koef * other[curstr]
                    col = n
        unisolution = True
        for i in range(m - 1, -1, -1):
            if self.strings[i] == [0] * n and other[i] != 0:
                unisolution = False
                break
            elif self.strings[i].count(0.0) < n - 1:
                unisolution = False
                break
            else:
                for j in range(n):
                    if self.strings[i][j] != 0:
                        other[i] /= self.strings[i][j]
                        break
        if not unisolution:
            raise MatrixError(self, other)
        return other


exec(stdin.read())
