import random
from random import choice, randint


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

    def add_tile(self):
        r = random.choice(self.rand)
        tile_x = random.randint(0, len(self.table) - 1)
        tile_y = random.randint(0, len(self.table) - 1)
        while self.table[tile_x][tile_y] != 0:
            tile_x = random.randint(0, len(self.table) - 1)
            tile_y = random.randint(0, len(self.table) - 1)
        self.table[tile_x][tile_y] = r

    def check_lose_or_win(self):
        for i in range(4):
            for j in range(4):
                if self.table[i][j] == 2048:
                    return 'win'
        for i in range(4):
            for j in range(4):
                if mat[i][j] == 0:
                    return 'it`s not over'

        for i in range(0, 3):
            for j in range(0, 3):
                if self.table[i][j] == self.table[i + 1][j] or self.table[i][j + 1] == self.table[i][j]:
                    return 'it`s not over'
        for k in range(0, 3):
            if self.table[3][k] == self.table[3][k + 1]:
                return 'it`s not over'
        for j in range(0, 3):
            if self.table[j][3] == self.table[j + 1][3]:
                return 'it`s not over'
        return 'lose'

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

    def move_up(self):
        self.transpose()
        self.cover_up()
        self.merge()
        self.cover_up()
        self.transpose()

    def move_down(self):
        self.transpose()
        self.reverse()
        self.cover_up()
        self.merge()
        self.cover_up()
        self.reverse()
        self.transpose()

    def move_left(self):
        self.cover_up()
        self.merge()
        self.cover_up()

    def move_right(self):
        self.reverse()
        self.cover_up()
        self.merge()
        self.cover_up()
        self.reverse()
