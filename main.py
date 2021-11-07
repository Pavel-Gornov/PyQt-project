import sys
from logic import Game
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QPixmap


class Example(QMainWindow, Game):
    def __init__(self):
        super().__init__()
        uic.loadUi('style.ui', self)
        self.block = False
        self.temp = QPixmap("0.png")
        self.pm = QPixmap("0.png")
        self.pm1 = QPixmap("1.png")
        self.pmyou = QPixmap("you.png")
        self.pmlose = QPixmap("lose.png")
        self.pmwin = QPixmap("win.png")
        self.l1.setPixmap(self.pm)
        self.l2.setPixmap(self.pm)
        self.l3.setPixmap(self.pm)
        self.l4.setPixmap(self.pm)
        self.l5.setPixmap(self.pm)
        self.l6.setPixmap(self.pm)
        self.l7.setPixmap(self.pm)
        self.l8.setPixmap(self.pm)
        self.l9.setPixmap(self.pm)
        self.l10.setPixmap(self.pm)
        self.l11.setPixmap(self.pm)
        self.l12.setPixmap(self.pm)
        self.l13.setPixmap(self.pm)
        self.l14.setPixmap(self.pm)
        self.l15.setPixmap(self.pm)
        self.l16.setPixmap(self.pm)
        self.lname.setPixmap(self.pm1)
        self.btn_up.clicked.connect(self.move_up)
        self.btn_down.clicked.connect(self.move_down)
        self.btn_left.clicked.connect(self.move_left)
        self.btn_right.clicked.connect(self.move_right)
        self.btn_rest.clicked.connect(self.restart)

    def win(self):
        self.l6.setPixmap(self.pmyou)
        self.l7.setPixmap(self.pmwin)
        self.block = True

    def lose(self):
        self.l6.setPixmap(self.pmyou)
        self.l7.setPixmap(self.pmlose)
        self.block = True

    def restart(self):
        self.new_game()
        self.vis()
        self.block = False

    def vis(self):
        for i in range(4):
            for j in range(4):
                a = self.table[i][j]
                n = j + (i * 4)
                if n == 0:
                    self.temp = QPixmap(f"{a}.png")
                    self.l1.setPixmap(self.temp)
                elif n == 1:
                    self.temp = QPixmap(f"{a}.png")
                    self.l2.setPixmap(self.temp)
                elif n == 2:
                    self.temp = QPixmap(f"{a}.png")
                    self.l3.setPixmap(self.temp)
                elif n == 3:
                    self.temp = QPixmap(f"{a}.png")
                    self.l4.setPixmap(self.temp)
                elif n == 4:
                    self.temp = QPixmap(f"{a}.png")
                    self.l5.setPixmap(self.temp)
                elif n == 5:
                    self.temp = QPixmap(f"{a}.png")
                    self.l6.setPixmap(self.temp)
                elif n == 6:
                    self.temp = QPixmap(f"{a}.png")
                    self.l7.setPixmap(self.temp)
                elif n == 7:
                    self.temp = QPixmap(f"{a}.png")
                    self.l8.setPixmap(self.temp)
                elif n == 8:
                    self.temp = QPixmap(f"{a}.png")
                    self.l9.setPixmap(self.temp)
                elif n == 9:
                    self.temp = QPixmap(f"{a}.png")
                    self.l10.setPixmap(self.temp)
                elif n == 10:
                    self.temp = QPixmap(f"{a}.png")
                    self.l11.setPixmap(self.temp)
                elif n == 11:
                    self.temp = QPixmap(f"{a}.png")
                    self.l12.setPixmap(self.temp)
                elif n == 12:
                    self.temp = QPixmap(f"{a}.png")
                    self.l13.setPixmap(self.temp)
                elif n == 13:
                    self.temp = QPixmap(f"{a}.png")
                    self.l14.setPixmap(self.temp)
                elif n == 14:
                    self.temp = QPixmap(f"{a}.png")
                    self.l15.setPixmap(self.temp)
                elif n == 15:
                    self.temp = QPixmap(f"{a}.png")
                    self.l16.setPixmap(self.temp)

    def move_up(self):
        if not self.block:
            self.transpose()
            self.cover_up()
            self.merge()
            self.cover_up()
            self.transpose()
            self.add_tile()
            if not self.block:
                self.vis()

    def move_down(self):
        if not self.block:
            self.check_lose_or_win()
            self.transpose()
            self.reverse()
            self.cover_up()
            self.merge()
            self.cover_up()
            self.reverse()
            self.transpose()
            self.add_tile()
            if not self.block:
                self.vis()

    def move_left(self):
        if not self.block:
            self.check_lose_or_win()
            self.cover_up()
            self.merge()
            self.cover_up()
            self.add_tile()
            if not self.block:
                self.vis()

    def move_right(self):
        if not self.block:
            self.check_lose_or_win()
            self.reverse()
            self.cover_up()
            self.merge()
            self.cover_up()
            self.reverse()
            self.add_tile()
            if not self.block:
                self.vis()

    def check_lose_or_win(self):
        a, b, c, d = False, False, False, False
        for i in range(4):
            for j in range(4):
                if self.table[i][j] == 2048:
                    self.win()
        for i in range(4):
            for j in range(4):
                if self.table[i][j] == 0:
                    a = True
                    break
        for i in range(3):
            for j in range(3):
                if self.table[i][j] == self.table[i + 1][j] or self.table[i][j + 1] == self.table[i][j]:
                    b = True
                    break
        for k in range(3):
            if self.table[3][k] == self.table[3][k + 1]:
                c = True
                break
        for j in range(3):
            if self.table[j][3] == self.table[j + 1][3]:
                d = True
                break
        if not a and not b and not c and not d:
            self.lose()

    def add_tile(self):
        a = False
        for i in range(4):
            for j in range(4):
                if self.table[i][j] == 0:
                    a = True
        if not a:
            self.lose()
        else:
            r = random.choice(self.rand)
            tile_x = random.randint(0, len(self.table) - 1)
            tile_y = random.randint(0, len(self.table) - 1)
            while self.table[tile_x][tile_y] != 0:
                tile_x = random.randint(0, len(self.table) - 1)
                tile_y = random.randint(0, len(self.table) - 1)
            self.table[tile_x][tile_y] = r


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
