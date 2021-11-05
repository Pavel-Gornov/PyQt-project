import sys
from logic import Game
from random import choice, randint
from PIL import Image
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QPixmap


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.image1 = Image.open("textures.png").resize((100, 100))
        self.image1.save("temp.png")
        self.pm = QPixmap("temp.png")
        self.pm1 = QPixmap("1.png")
        self.label.setPixmap(self.pm)
        self.label_2.setPixmap(self.pm)
        self.label_3.setPixmap(self.pm)
        self.label_4.setPixmap(self.pm)
        self.label_5.setPixmap(self.pm)
        self.label_6.setPixmap(self.pm)
        self.label_7.setPixmap(self.pm)
        self.label_8.setPixmap(self.pm)
        self.label_9.setPixmap(self.pm)
        self.label_10.setPixmap(self.pm)
        self.label_11.setPixmap(self.pm)
        self.label_12.setPixmap(self.pm)
        self.label_13.setPixmap(self.pm)
        self.label_14.setPixmap(self.pm)
        self.label_15.setPixmap(self.pm)
        self.label_16.setPixmap(self.pm)
        self.label_17.setPixmap(self.pm1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
