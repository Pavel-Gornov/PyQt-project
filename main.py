import sys
import time
from logic import Game
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLCDNumber, QDialog, QCheckBox, \
    QRadioButton, QScrollBar
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize, Qt


class Example(QMainWindow, Game):
    def __init__(self):
        super().__init__()
        uic.loadUi('style.ui', self)
        global savedmap2
        self.titles = ['2^11', '2048', '2048?', '2048: моя версия', 'ДВЕ ТЫСЯЧИ СОРОК ВОСЕМЬ!', '2000 + 40 + 8',
                       'проект QT!', 'TWO THOUSAND AND FORTY-EIGHT', 'при каждом запуске разноые заголовки!',
                       '1024 * 2', '2 ** 11', 'игра про сложение плиток.....']
        self.setFixedSize(501, 785)
        self.setWindowTitle(random.choice(self.titles))
        self.block = False
        self.temp = QPixmap("0.png")
        self.pm = QPixmap("0.png")
        self.pm1 = QPixmap("1.png")
        self.pmyou = QPixmap("you.png")
        self.pmlose = QPixmap("lose.png")
        self.pmwin = QPixmap("win.png")
        self.btn_rest.setIcon(QIcon("restart.png"))
        self.btn_rest.setIconSize(QSize(75, 75))
        self.btn_setings.setIcon(QIcon("settings.png"))
        self.btn_setings.setIconSize(QSize(75, 75))
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
        self.table = savedmap2
        self.vis()
        self.score()
        self.btn_up.clicked.connect(self.move_up)
        self.btn_down.clicked.connect(self.move_down)
        self.btn_left.clicked.connect(self.move_left)
        self.btn_right.clicked.connect(self.move_right)
        self.btn_rest.clicked.connect(self.restart)
        self.btn_setings.clicked.connect(self.settings)

    def win(self):
        self.l6.setPixmap(self.pmyou)
        self.l7.setPixmap(self.pmwin)
        self.block = True
        self.score()

    def lose(self):
        self.l6.setPixmap(self.pmyou)
        self.l7.setPixmap(self.pmlose)
        self.block = True
        self.score()

    def restart(self):
        self.new_game()
        self.vis()
        self.block = False
        self.score()

    def vis(self):
        global is_save
        global savedmap2

        if is_save:
            savedmap2 = self.table
            f1 = open('save.txt', encoding='utf8', mode='wt')
            f1.write(str(is_save) + '\n')
            f1.write(str(savedmap2).replace('[', '').replace(']', '').replace(',', ''))
            f1.close()
        else:
            f1 = open('save.txt', encoding='utf8', mode='wt')
            f1.write(str(is_save) + '\n')
            f1.write(str('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'))
            f1.close()
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

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W:
            self.move_up()
        if event.key() == Qt.Key_S:
            self.move_down()
        if event.key() == Qt.Key_A:
            self.move_left()
        if event.key() == Qt.Key_D:
            self.move_right()

    def move_up(self):
        if not self.block:
            self.transpose()
            self.cover_up()
            self.merge()
            self.cover_up()
            self.transpose()
            self.add_tile()
            self.score()
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
            self.score()
            if not self.block:
                self.vis()

    def move_left(self):
        if not self.block:
            self.check_lose_or_win()
            self.cover_up()
            self.merge()
            self.cover_up()
            self.add_tile()
            self.score()
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
            self.score()
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

    def score(self):
        score = 0
        for i in self.table:
            score += sum(i)
        self.lcd_score.display(score)
        self.record()

    def record(self):
        if self.lcd_score.intValue() > self.lcd_record.intValue():
            self.lcd_record.display(self.lcd_score.intValue())

    def settings(self):
        global is_auto
        dialog = Dialog()
        dialog.exec_()
        self.vis()
        if is_auto:
            self.auto_mode()
            is_auto = False

    def auto_mode(self):
        while not self.block:
            s = random.randint(1, 4)
            if s == 1:
                self.move_up()
            if s == 2:
                self.move_down()
            if s == 3:
                self.move_left()
            if s == 4:
                self.move_right()


class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        global is_save
        uic.loadUi('settings.ui', self)
        self.setFixedSize(400, 300)
        self.setWindowTitle('Настройки')
        self.btn_c.clicked.connect(self.ex)
        self.btn_a.clicked.connect(self.apply)
        self.save.setChecked(is_save)

    def apply(self):
        global is_save
        global is_auto
        is_auto = self.auto_mode.isChecked()
        is_save = self.save.isChecked()
        if not is_save:
            f1 = open('save.txt', encoding='utf8', mode='wt')
            f1.write(str(is_save) + '\n')
            f1.write(str('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'))
            f1.close()
        self.close()

    a = False

    def ex(self):
        self.close()


if __name__ == '__main__':
    is_auto = False
    f = open('save.txt', encoding='utf8')
    text = f.readlines()
    f.close()
    p2 = list()
    for i in text:
        p = ''.join(i.split('\n')).split()
        p2.append(p)
    if p2[0] == ['False']:
        is_save = False
    else:
        is_save = True
    savedmap = p2[1::]
    savedmap = savedmap[0]
    savedmap2 = [[], [], [], []]
    c = 0
    for i in range(4):
        for j in range(4):
            savedmap2[i].append(int(savedmap[j + c]))
        c += 4
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
