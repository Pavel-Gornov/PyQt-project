class Game:
    def __init__(self):
        self.table = list()
        for _ in range(4):
            self.table.append([0, 0, 0, 0])
        self.rand = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]

    def new_game(self):
        self.table = list()
        for _ in range(4):
            self.table.append([0, 0, 0, 0])

    def reverse(self):
        reverse = list()
        for i in range(4):
            reverse.append([])
            for j in range(4):
                reverse[i].append(self.table[i][3 - j])
        self.table = reverse

    def transpose(self):
        transpose = list()
        for i in range(4):
            transpose.append([])
            for j in range(4):
                transpose[i].append(self.table[j][i])
        self.table = transpose

    def cover_up(self):
        new = list()
        for j in range(4):
            partial_new = list()
            for i in range(4):
                partial_new.append(0)
            new.append(partial_new)
        for i in range(4):
            count = 0
            for j in range(4):
                if self.table[i][j] != 0:
                    new[i][count] = self.table[i][j]
                    count += 1
        self.table = new

    def merge(self):
        for i in range(4):
            for j in range(3):
                if self.table[i][j] == self.table[i][j + 1] and self.table[i][j] != 0:
                    self.table[i][j] *= 2
                    self.table[i][j + 1] = 0
