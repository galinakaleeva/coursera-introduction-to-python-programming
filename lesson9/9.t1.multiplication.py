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

    __rmul__ = __mul__


exec(stdin.read())
