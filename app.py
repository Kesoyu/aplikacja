import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('okno.ui', self)


app = QApplication(sys.argv)
app.setStyleSheet('''

''')

if __name__ == "__main__":
    window = MyApp()
    window.show()

    app.exec()