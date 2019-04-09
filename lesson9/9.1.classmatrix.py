from sys import stdin
import copy


class Matrix:
    def __init__(self, strings=[[]]):
        self.strings = copy.deepcopy(strings)

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
        return (len(self.strings), len(self.strings[0]))

exec(stdin.read())
