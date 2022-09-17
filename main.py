import webbrowser
import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QWidget

webbrowser.open('https://sites.google.com/view/hellowelcometomysoftwareworld/%E0%B8%AB%E0%B8%99%E0%B8%B2%E0%B9%81%E0%B8%A3%E0%B8%81')

def calculate_color_price(color):
    if color == 'red':
        return 20
    elif color == 'gray':
        return 40
    elif color == 'gold':
        return 60
    elif color == 'black':
        return 80

class Widget(QWidget):
    def on_button_red_clicked(self):
        self.price += calculate_color_price('red')
        self.label.setText(f'Price: {self.price}')

    def on_button_grey_clicked(self):
        self.price += calculate_color_price('gray')
        self.label.setText(f'Price: {self.price}')

    def on_button_gold_clicked(self):
        self.price += calculate_color_price('gold')
        self.label.setText(f'Price: {self.price}')

    def on_button_black_clicked(self):
        self.price += calculate_color_price('black')
        self.label.setText(f'Price: {self.price}')

    def on_button_clear_clicked(self):
        self.price = 0
        self.label.setText(f'Price: {self.price}')

    def __init__(self):
        super().__init__()
        self.price = 0

        # create ui without loading from file
        self.button_red = QtWidgets.QPushButton('Red', self)
        self.button_red.move(20, 20)
        self.button_red.clicked.connect(self.on_button_red_clicked)

        self.button_grey = QtWidgets.QPushButton('Grey', self)
        self.button_grey.move(20, 60)
        self.button_grey.clicked.connect(self.on_button_grey_clicked)

        self.button_gold = QtWidgets.QPushButton('Gold', self)
        self.button_gold.move(20, 100)
        self.button_gold.clicked.connect(self.on_button_gold_clicked)

        self.button_black = QtWidgets.QPushButton('Black', self)
        self.button_black.move(20, 140)
        self.button_black.clicked.connect(self.on_button_black_clicked)

        self.button_clear = QtWidgets.QPushButton('Clear', self)
        self.button_clear.move(20, 180)
        self.button_clear.clicked.connect(self.on_button_clear_clicked)


        self.label = QtWidgets.QLabel('Price: 0', self)
        self.label.move(20, 220)
        # size of label
        self.label.resize(200, 20)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('โปรแกรมคำนวนราคาซุชิ')
        self.show()

    def closeEvent(self, event):
        webbrowser.open(
            "https://sites.google.com/view/thecredit/%E0%B8%AB%E0%B8%99%E0%B8%B2%E0%B9%81%E0%B8%A3%E0%B8%81")
        event.accept()

app = QApplication(sys.argv)
widget = Widget()
sys.exit(app.exec())